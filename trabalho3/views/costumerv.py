from django.shortcuts import render, redirect
from trabalho3.forms.costumerf import CostumerForm
from trabalho3.models.costumer import Costumer


def emp(request):
    if request.method == "POST":
        form = CostumerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/costumer/list/costumers/')
            except:
                pass
    else:
        form = CostumerForm()
    return render(request, '../templates/costumer/create_costumer.html', {'form': form})


def show(request):
    costumers = Costumer.objects.all()
    return render(request, '../templates/costumer/list_costumers.html', {'costumers': costumers})


def edit(request, id):
    costumer = Costumer.objects.get(id=id)
    return render(request, '../templates/costumer/edit_costumer.html', {'costumer': costumer})


def update(request, id):
    costumer = Costumer.objects.get(id=id)
    form = CostumerForm(request.POST, instance=costumer)
    if form.is_valid():
        form.save()
        return redirect('/costumer/list/costumers/')
    return render(request, '../templates/costumer/edit_costumer.html', {'costumer': costumer})


def destroy(request, id):
    costumer = Costumer.objects.get(id=id)
    costumer.delete()
    return redirect('/costumer/list/costumers/')
