from django.shortcuts import render, redirect
from trabalho3.forms.billf import BillForm
from trabalho3.models.bill import Bill
from trabalho3.models.costumer import Costumer
from trabalho3.models.provider import Provider


def emp(request):
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/bill/list/bills/')
            except:
                pass
    else:
        form = BillForm()
    return render(request, '../templates/bill/create_bill.html', {'form': form})


def show(request):
    bills = Bill.objects.all()
    return render(request, '../templates/bill/list_bills.html', {'bills': bills})


def edit(request, id):
    bill = Bill.objects.get(id=id)
    return render(request, '../templates/bill/edit_bill.html', {'bill': bill})


def update(request, id):
    bill = Bill.objects.get(id=id)
    costumers = Costumer.objects.all()
    providers = Provider.objects.all()
    form = BillForm(request.POST, instance=bill)
    if form.is_valid():
        form.save()
        return redirect('/bill/list/bills/')
    return render(request, '../templates/bill/edit_bill.html',
                  {'bill': bill, 'costumers': costumers, 'providers': providers})


def destroy(request, id):
    bill = Bill.objects.get(id=id)
    bill.delete()
    return redirect('/bill/list/bills/')
