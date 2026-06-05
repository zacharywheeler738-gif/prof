from django.db import models

class PaymentConfig(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    gateway = models.CharField(max_length=100)
