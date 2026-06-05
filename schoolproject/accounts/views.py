from django.shortcuts import render
from .models import PaymentConfig

def payment_page(request):
    config = PaymentConfig.objects.first()

    return render(request, "payment.html", {
        "config": config
    })