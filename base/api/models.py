from django.db import models

from django.db import models

class Company(models.Model):
    inn = models.CharField(max_length=12, unique=True)
    revenue = models.DecimalField(max_digits=15, decimal_places=2)  # Выручка
    cost_of_sales = models.DecimalField(max_digits=15, decimal_places=2)  # Себестоимость
    gross_profit = models.DecimalField(max_digits=15, decimal_places=2)  # Валовая прибыль
    commercial_expenses = models.DecimalField(max_digits=15, decimal_places=2)  # Коммерческие расходы
    administrative_expenses = models.DecimalField(max_digits=15, decimal_places=2)  # Управленческие расходы
    pre_tax_profit = models.DecimalField(max_digits=15, decimal_places=2)  # Прибыль до налогообложения
    tax = models.DecimalField(max_digits=15, decimal_places=2)  # Налог на прибыль
    net_profit = models.DecimalField(max_digits=15, decimal_places=2)  # Чистая прибыль
    total_assets = models.DecimalField(max_digits=15, decimal_places=2)  # Активы
    non_current_assets = models.DecimalField(max_digits=15, decimal_places=2)  # Внеоборотные активы
    current_assets = models.DecimalField(max_digits=15, decimal_places=2)  # Оборотные активы
    equity = models.DecimalField(max_digits=15, decimal_places=2)  # Капитал и резервы
    long_term_liabilities = models.DecimalField(max_digits=15, decimal_places=2)  # Долгосрочные обязательства
    short_term_liabilities = models.DecimalField(max_digits=15, decimal_places=2)  # Краткосрочные обязательства
    total_liabilities = models.DecimalField(max_digits=15, decimal_places=2)  # Пассивы

    def __str__(self):
        return self.inn