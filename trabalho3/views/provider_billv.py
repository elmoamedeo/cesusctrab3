from django.shortcuts import render, redirect
from trabalho3.forms.provider_billf import ProviderBillForm
from trabalho3.models.provider_bill import ProviderBill
from trabalho3.models.costumer import Costumer
from trabalho3.models.provider import Provider


def emp(request):
    if request.method == "POST":
        form = ProviderBillForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/provider_bill/list/provider_bills/')
            except:
                pass
    else:
        form = ProviderBillForm()
    return render(request, '../templates/provider_bill/create_bill.html', {'form': form})


def show(request):
    provider_bills = ProviderBill.objects.all()
    provider_bill_products = ProviderBill.product.through.objects.all()
    return render(request, '../templates/provider_bill/list_bills.html',
                  {'provider_bills': provider_bills, 'provider_bill_products': provider_bill_products})


def edit(request, id):
    provider_bill = ProviderBill.objects.get(id=id)
    return render(request, '../templates/provider_bill/edit_bill.html', {'provider_bill': provider_bill})


def update(request, id):
    provider_bill = ProviderBill.objects.get(id=id)
    costumers = Costumer.objects.all()
    providers = Provider.objects.all()
    form = ProviderBillForm(request.POST, instance=provider_bill)
    if form.is_valid():
        form.save()
        return redirect('/provider_bill/list/provider_bills/')
    return render(request, '../templates/provider_bill/edit_bill.html',
                  {'provider_bill': provider_bill, 'costumers': costumers, 'providers': providers})


def destroy(request, id):
    provider_bill = ProviderBill.objects.get(id=id)
    provider_bill.delete()
    return redirect('/provider_bill/list/provider_bills/')
