from django.shortcuts import render, redirect
from trabalho3.forms.provider_billf import ProviderBillForm
from trabalho3.models.provider_bill import ProviderBill
from trabalho3.models.provider import Provider
from trabalho3.models.product import Product


def emp(request):
    products = Product.objects.all()
    if request.method == "POST":
        form = ProviderBillForm(request.POST)
        if form.is_valid():
            try:
                # Get's all selected products
                for product in form['product'].value():
                    # Update product quantity based on how many items were taken in the bill
                    provider_bill_product = Product.objects.get(id=product)
                    if int(form['quantity'].value()) > provider_bill_product.quantity:
                        form.clean()
                        return render(request, '../templates/provider_bill/create_bill.html',
                                      {'alert_flag': True, 'form': form, 'products': products})
                    provider_bill_product.quantity = provider_bill_product.quantity - int(form['quantity'].value())
                    provider_bill_product.save()

                form.save()
                return redirect('/provider_bill/list/provider_bills/')
            except:
                pass
    else:
        form = ProviderBillForm()
    return render(request, '../templates/provider_bill/create_bill.html', {'form': form, 'products': products})


def show(request):
    # Get's all provider bills
    provider_bills = ProviderBill.objects.all()

    # Get's products trough many-to-many relationship
    provider_bill_products = ProviderBill.product.through.objects.all()

    # Get's all providers
    providers = Provider.objects.all()

    return render(request, '../templates/provider_bill/list_bills.html',
                  {'provider_bills': provider_bills, 'provider_bill_products': provider_bill_products,
                   'providers': providers})


def edit(request, id):
    provider_bill = ProviderBill.objects.get(id=id)
    return render(request, '../templates/provider_bill/edit_bill.html', {'provider_bill': provider_bill})


def update(request, id):
    provider_bill = ProviderBill.objects.get(id=id)
    provider_bill_products = ProviderBill.product.through.objects.all()
    products = Product.objects.all()
    form = ProviderBillForm(request.POST, instance=provider_bill)
    if form.is_valid():
        # Get's old provider bill value and checks if the new quantity is higher than the older
        # If that's the case, the difference get's subtracted from the total product quantity
        for product_form in form['product'].value():
            old_provider_bill = ProviderBill.objects.get(id=id)
            if int(form['quantity'].value()) > old_provider_bill.quantity:
                provider_bill_product = Product.objects.get(id=int(product_form))
                form_value_difference = int(form['quantity'].value()) - old_provider_bill.quantity
                if form_value_difference > provider_bill_product.quantity:
                    form.clean()
                    return render(request, '../templates/provider_bill/edit_bill.html',
                                  {'alert_flag': True, 'provider_bill': provider_bill,
                                   'provider_bill_products': provider_bill_products,
                                   'products': products})
                provider_bill_product.quantity = provider_bill_product.quantity - (
                    form_value_difference)
                provider_bill_product.save()
        form.save()
        return redirect('/provider_bill/list/provider_bills/')
    return render(request, '../templates/provider_bill/edit_bill.html',
                  {'provider_bill': provider_bill, 'provider_bill_products': provider_bill_products,
                   'products': products})


def destroy(request, id):
    provider_bill = ProviderBill.objects.get(id=id)
    provider_bill.delete()
    return redirect('/provider_bill/list/provider_bills/')
