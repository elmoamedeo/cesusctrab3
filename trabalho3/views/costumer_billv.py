from django.shortcuts import render, redirect
from trabalho3.forms.costumer_billf import CostumerBillForm
from trabalho3.models.costumer_bill import CostumerBill
from trabalho3.models.costumer import Costumer


def emp(request):
    if request.method == "POST":
        form = CostumerBillForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/costumer_bill/list/costumer_bills/')
            except:
                pass
    else:
        form = CostumerBillForm()
    return render(request, '../templates/costumer_bill/create_bill.html', {'form': form})


def show(request):
    costumer_bills = CostumerBill.objects.all()
    costumer_bill_products = CostumerBill.product.through.objects.all()
    return render(request, '../templates/costumer_bill/list_bills.html',
                  {'costumer_bills': costumer_bills, 'costumer_bill_products': costumer_bill_products})


def edit(request, id):
    costumer_bill = CostumerBill.objects.get(id=id)
    return render(request, '../templates/costumer_bill/edit_bill.html', {'costumer_bill': costumer_bill})


def update(request, id):
    costumer_bill = CostumerBill.objects.get(id=id)
    costumers = Costumer.objects.all()
    form = CostumerBillForm(request.POST, instance=costumer_bill)
    if form.is_valid():
        form.save()
        return redirect('/costumer_bill/list/costumer_bills/')
    return render(request, '../templates/costumer_bill/edit_bill.html',
                  {'costumer_bill': costumer_bill, 'costumers': costumers})


def destroy(request, id):
    costumer_bill = CostumerBill.objects.get(id=id)
    costumer_bill.delete()
    return redirect('/costumer_bill/list/costumer_bills/')
