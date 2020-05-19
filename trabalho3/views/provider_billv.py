from django.shortcuts import render, redirect
from trabalho3.forms.provider_billf import ProviderBillForm
from trabalho3.forms.productf import ProductForm
from trabalho3.models.provider_bill import ProviderBill
from trabalho3.models.costumer import Costumer
from trabalho3.models.provider import Provider
from trabalho3.models.product import Product


def emp(request):
    if request.method == "POST":
        form = ProviderBillForm(request.POST)
        if form.is_valid():
            try:
                for product in form.data.product:
                    # Update product quantity based on how many items were taken in the bill
                    provider_bill_product = Product.objects.get(id=product.id)
                    product_form = ProductForm(request.POST, instance=provider_bill_product)
                    product_form.quantity = provider_bill_product.quantity - form.quantity
                    product_form.save()

                form.save()
                return redirect('/provider_bill/list/provider_bills/')
            except:
                pass
    else:
        form = ProviderBillForm()
    return render(request, '../templates/provider_bill/create_bill.html', {'form': form})


def show(request):
    # Get's all provider bills
    provider_bills = ProviderBill.objects.all()
    print(provider_bills.values())

    # Get's products trough many-to-many relationship
    provider_bill_products = ProviderBill.product.through.objects.all()
    print(provider_bill_products.values())

    # Get's all providers
    providers = Provider.objects.all()
    print(providers.values())

    return render(request, '../templates/provider_bill/list_bills.html',
                  {'provider_bills': provider_bills, 'provider_bill_products': provider_bill_products,
                   'providers': providers})


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
