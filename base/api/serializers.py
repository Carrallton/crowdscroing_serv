from rest_framework import serializers
from .models import Company, FinancialReport

class FinancialReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialReport
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    reports = FinancialReportSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['inn', 'name', 'reports']