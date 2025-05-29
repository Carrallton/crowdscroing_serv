import pandas as pd
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import Company, FinancialReport
from .serializers import CompanySerializer
import logging

logger = logging.getLogger(__name__)


class CompanyDetailView(APIView):
    def get(self, request, inn):
        try:
            company = Company.objects.get(inn=inn)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response({"error": "Компания не найдена"}, status=404)

class UploadExcelFileView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES.get('file')
        inn = request.data.get('inn')
        year = request.data.get('year')  # Новый параметр: год отчета

        if not file:
            return Response({"error": "Файл не выбран"}, status=400)

        if not inn or len(inn) != 10:
            return Response({"error": "Введите корректный ИНН (10 цифр)"}, status=400)

        if not year or not year.isdigit():
            return Response({"error": "Укажите год отчета"}, status=400)

        try:
            df_income = pd.read_excel(file, sheet_name='Отчет о фин. результатах', header=None)
            df_balance = pd.read_excel(file, sheet_name='Бухгалтерский баланс', header=None)
        except Exception as e:
            logger.error(f"Ошибка при чтении файла: {e}")
            return Response({"error": f"Ошибка при чтении файла: {str(e)}"}, status=400)

        def get_value_by_code(df, code):
            for index, row in df.iterrows():
                if str(row[1]).strip() == str(code).strip():
                    value = row[2]
                    if isinstance(value, str):
                        value = value.replace(" ", "").replace(",", ".")
                    try:
                        return float(value)
                    except:
                        logger.warning(f"Значение для кода {code} не является числом: {value}")
                        return 0
            logger.warning(f"Не найдено значение для кода {code}")
            return 0

        company, created = Company.objects.update_or_create(
            inn=inn,
            defaults={'name': f'Компания {inn}'}
        )

        report_data = {
            'company': company,
            'year': int(year),
            'revenue': get_value_by_code(df_income, '2110'),
            'cost_of_sales': get_value_by_code(df_income, '2120'),
            'gross_profit': get_value_by_code(df_income, '2100'),
            'commercial_expenses': get_value_by_code(df_income, '2210'),
            'administrative_expenses': get_value_by_code(df_income, '2220'),
            'pre_tax_profit': get_value_by_code(df_income, '2200'),
            'tax': get_value_by_code(df_income, '2410'),
            'net_profit': get_value_by_code(df_income, '2400'),
            'total_assets': get_value_by_code(df_balance, '1600'),
            'non_current_assets': get_value_by_code(df_balance, '1100'),
            'current_assets': get_value_by_code(df_balance, '1200'),
            'equity': get_value_by_code(df_balance, '1300'),
            'long_term_liabilities': get_value_by_code(df_balance, '1400'),
            'short_term_liabilities': get_value_by_code(df_balance, '1500'),
            'total_liabilities': get_value_by_code(df_balance, '1700'),
        }

        report, _ = FinancialReport.objects.update_or_create(
            company=report_data['company'],
            year=report_data['year'],
            defaults=report_data
        )

        return Response({
            "status": "success",
            "message": f"Отчет компании {inn} за {year} год добавлен/обновлён"
        })