from django.shortcuts import render, redirect
from trabalho3.models.costumer_bill import CostumerBill


def show(request):
    costumer_bill_products = CostumerBill.product.through.objects.all()
    costumer_bills = CostumerBill.objects.all()
    return render(request, '../templates/billcostumer_product/list_bills.html',
                  {'costumer_bill_products': costumer_bill_products, 'costumer_bills': costumer_bills})


def destroy(request, id):
    costumer_bill_product = CostumerBill.objects.get(id=id)
    costumer_bill_product.delete()
    return redirect('/costumer_bill_product/list/costumer_bill_products/')