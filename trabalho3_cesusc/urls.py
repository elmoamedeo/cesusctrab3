from django.contrib import admin
from django.urls import path
# Model views
from trabalho3.views import employeev as employee
from trabalho3.views import productv as product
from trabalho3.views import costumerv as costumer
from trabalho3.views import billv as bill
from trabalho3.views import providerv as provider

urlpatterns = [
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
    # Bill paths
    path('bill/', bill.emp),
    path('bill/list/bills/', bill.show),
    path('bill/edit/<int:id>', bill.edit),
    path('bill/update/<int:id>', bill.update),
    path('bill/delete/<int:id>', bill.destroy),
    # Provider paths
    path('provider/', provider.emp),
    path('provider/list/providers/', provider.show),
    path('costumer/edit/<int:id>', provider.edit),
    path('costumer/update/<int:id>', provider.update),
    path('costumer/delete/<int:id>', provider.destroy),
]
