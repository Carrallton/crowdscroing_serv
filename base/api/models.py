from django.db import models

class Company(models.Model):
    inn = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=255, default="Неизвестная компания")

    def __str__(self):
        return f"{self.name} ({self.inn})"

class FinancialReport(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='reports')
    year = models.PositiveIntegerField()
    revenue = models.DecimalField(max_digits=15, decimal_places=2)
    cost_of_sales = models.DecimalField(max_digits=15, decimal_places=2)
    gross_profit = models.DecimalField(max_digits=15, decimal_places=2)
    commercial_expenses = models.DecimalField(max_digits=15, decimal_places=2)
    administrative_expenses = models.DecimalField(max_digits=15, decimal_places=2)
    pre_tax_profit = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.DecimalField(max_digits=15, decimal_places=2)
    net_profit = models.DecimalField(max_digits=15, decimal_places=2)
    total_assets = models.DecimalField(max_digits=15, decimal_places=2)
    non_current_assets = models.DecimalField(max_digits=15, decimal_places=2)
    current_assets = models.DecimalField(max_digits=15, decimal_places=2)
    equity = models.DecimalField(max_digits=15, decimal_places=2)
    long_term_liabilities = models.DecimalField(max_digits=15, decimal_places=2)
    short_term_liabilities = models.DecimalField(max_digits=15, decimal_places=2)
    total_liabilities = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.company.name} - {self.year}"