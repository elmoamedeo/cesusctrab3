from django.shortcuts import render
from trabalho3.models.provider_bill import ProviderBill


def show(request):
    provider_bill_products = ProviderBill.product.through.objects.all()
    provider_bills = ProviderBill.objects.all()
    return render(request, '../templates/billprovider_product/list_bills.html',
                  {'provider_bill_products': provider_bill_products, 'provider_bills': provider_bills})
