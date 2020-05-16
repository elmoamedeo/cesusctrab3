from django.shortcuts import render, redirect
from trabalho3.forms.productf import ProductForm
from trabalho3.models.product import Product


def emp(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/product/list/products/')
            except:
                pass
    else:
        form = ProductForm()
    return render(request, '../templates/product/create_product.html', {'form': form})


def show(request):
    products = Product.objects.all()
    return render(request, '../templates/product/list_products.html', {'products': products})


def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request, '../templates/product/edit_product.html', {'product': product})


def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/product/list/products')
    return render(request, '../templates/product/edit_product.html', {'product': product})


def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/product/list/products')
