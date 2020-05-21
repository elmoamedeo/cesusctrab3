from django.shortcuts import render
from trabalho3.models.costumer_bill import CostumerBill


def show(request):
    costumer_bill_products = CostumerBill.product.through.objects.all()
    costumer_bills = CostumerBill.objects.all()
    return render(request, '../templates/billcostumer_product/list_bills.html',
                  {'costumer_bill_products': costumer_bill_products, 'costumer_bills': costumer_bills})
