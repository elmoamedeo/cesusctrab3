from django.shortcuts import render, redirect
from trabalho3.forms.costumer_billf import CostumerBillForm
from trabalho3.models.costumer_bill import CostumerBill
from trabalho3.models.costumer import Costumer
from trabalho3.models.product import Product


def emp(request):
    products = Product.objects.all()
    if request.method == "POST":
        form = CostumerBillForm(request.POST)
        if form.is_valid():
            try:
                # Get's all selected products
                for product in form['product'].value():
                    # Update product quantity based on how many items were taken in the bill
                    costumer_bill_product = Product.objects.get(id=product)
                    if int(form['quantity'].value()) > costumer_bill_product.quantity:
                        form.clean()
                        return render(request, '../templates/costumer_bill/create_bill.html',
                                      {'alert_flag': True, 'form': form, 'products': products})
                    costumer_bill_product.quantity = costumer_bill_product.quantity - int(form['quantity'].value())
                    costumer_bill_product.save()

                form.save()
                return redirect('/costumer_bill/list/costumer_bills/')
            except:
                pass
    else:
        form = CostumerBillForm()
    return render(request, '../templates/costumer_bill/create_bill.html', {'form': form, 'products': products})


def show(request):
    # Get's all costumer bills
    costumer_bills = CostumerBill.objects.all()

    # Get's products trough many-to-many relationship
    costumer_bill_products = CostumerBill.product.through.objects.all()

    # Get's all providers
    costumers = Costumer.objects.all()

    return render(request, '../templates/costumer_bill/list_bills.html',
                  {'costumer_bills': costumer_bills, 'costumer_bill_products': costumer_bill_products,
                   'costumers': costumers})


def edit(request, id):
    costumer_bill = CostumerBill.objects.get(id=id)
    return render(request, '../templates/costumer_bill/edit_bill.html', {'costumer_bill': costumer_bill})


def update(request, id):
    costumer_bill = CostumerBill.objects.get(id=id)
    costumer_bill_products = CostumerBill.product.through.objects.all()
    costumers = Costumer.objects.all()
    products = Product.objects.all()
    form = CostumerBillForm(request.POST, instance=costumer_bill)
    if form.is_valid():
        # Get's old costumer bill value and checks if the new quantity is higher than the older
        # If that's the case, the difference get's subtracted from the total product quantity
        for product_form in form['product'].value():
            old_costumer_bill = CostumerBill.objects.get(id=id)
            if int(form['quantity'].value()) > old_costumer_bill.quantity:
                costumer_bill_product = Product.objects.get(id=int(product_form))
                form_value_difference = int(form['quantity'].value()) - old_costumer_bill.quantity
                if form_value_difference > costumer_bill_product.quantity:
                    form.clean()
                    return render(request, '../templates/costumer_bill/edit_bill.html',
                                  {'alert_flag': True, 'costumer_bill': costumer_bill,
                                   'costumer_bill_products': costumer_bill_products,
                                   'costumers': costumers,
                                   'products': products})
                costumer_bill_product.quantity = costumer_bill_product.quantity - (
                    form_value_difference)
                costumer_bill_product.save()
        form.save()
        return redirect('/costumer_bill/list/costumer_bills/')
    return render(request, '../templates/costumer_bill/edit_bill.html',
                  {'costumer_bill': costumer_bill,
                   'costumer_bill_products': costumer_bill_products,
                   'costumers': costumers,
                   'products': products})


def destroy(request, id):
    costumer_bill = CostumerBill.objects.get(id=id)
    costumer_bill.delete()
    return redirect('/costumer_bill/list/costumer_bills/')
