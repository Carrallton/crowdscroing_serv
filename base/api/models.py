from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, default="Неизвестная компания")
    revenue = models.DecimalField(max_digits=15, decimal_places=2)
    expenses = models.DecimalField(max_digits=15, decimal_places=2)
    profit = models.DecimalField(max_digits=15, decimal_places=2)
    debt = models.DecimalField(max_digits=15, decimal_places=2)
    assets = models.DecimalField(max_digits=15, decimal_places=2)
    liabilities = models.DecimalField(max_digits=15, decimal_places=2)
    rating = models.IntegerField(null=True, blank=True)
    credit_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name or "Без названия"