from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

# Model views
from trabalho3.views import employeev as employee
from trabalho3.views import productv as product
from trabalho3.views import costumerv as costumer
from trabalho3.views import providerv as provider
from trabalho3.views import costumer_billv as costumer_bill
from trabalho3.views import provider_billv as provider_bill
from trabalho3.views import costumer_bill_productv as costumer_bill_product
from trabalho3.views import provider_bill_productv as provider_bill_product

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name="home"),
    path('admin/', admin.site.urls),
    # Employee paths
    path('employee/', employee.emp),
    path('employee/list/employees/', employee.show),
    path('employee/edit/<int:id>', employee.edit),
    path('employee/update/<int:id>', employee.update),
    path('employee/delete/<int:id>', employee.destroy),
    # Product paths
    path('product/', product.emp),
    path('product/list/products/', product.show),
    path('product/edit/<int:id>', product.edit),
    path('product/update/<int:id>', product.update),
    path('product/delete/<int:id>', product.destroy),
    # Costumer paths
    path('costumer/', costumer.emp),
    path('costumer/list/costumers/', costumer.show),
    path('costumer/edit/<int:id>', costumer.edit),
    path('costumer/update/<int:id>', costumer.update),
    path('costumer/delete/<int:id>', costumer.destroy),
    # Costumer Bill paths
    path('costumer_bill/', costumer_bill.emp),
    path('costumer_bill/list/costumer_bills/', costumer_bill.show),
    path('costumer_bill/edit/<int:id>', costumer_bill.edit),
    path('costumer_bill/update/<int:id>', costumer_bill.update),
    path('costumer_bill/delete/<int:id>', costumer_bill.destroy),
    # Provider Bill paths
    path('provider_bill/', provider_bill.emp),
    path('provider_bill/list/provider_bills/', provider_bill.show),
    path('provider_bill/edit/<int:id>', provider_bill.edit),
    path('provider_bill/update/<int:id>', provider_bill.update),
    path('provider_bill/delete/<int:id>', provider_bill.destroy),
    # Costumer Bill Product paths
    path('costumer_bill_product/list/costumer_bill_products/', costumer_bill_product.show),
    # Provider Bill Product paths
    path('provider_bill_product/list/provider_bill_products/', provider_bill_product.show),
    # Provider paths
    path('provider/', provider.emp),
    path('provider/list/providers/', provider.show),
    path('provider/edit/<int:id>', provider.edit),
    path('provider/update/<int:id>', provider.update),
    path('provider/delete/<int:id>', provider.destroy),
]
