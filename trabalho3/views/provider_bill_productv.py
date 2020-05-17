from django.shortcuts import render, redirect
from trabalho3.models.provider_bill import ProviderBill


def show(request):
    provider_bill_products = ProviderBill.product.through.objects.all()
    provider_bills = ProviderBill.objects.all()
    return render(request, '../templates/billprovider_product/list_bills.html',
                  {'provider_bill_products': provider_bill_products, 'provider_bills': provider_bills})


def destroy(request, id):
    provider_bill_product = ProviderBill.objects.get(id=id)
    provider_bill_product.delete()
    return redirect('/provider_bill_product/list/provider_bill_products/')
