from django.shortcuts import render, redirect
from trabalho3.forms.providerf import ProviderForm
from trabalho3.models.provider import Provider


def emp(request):
    if request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/provider/list/providers/')
            except:
                pass
    else:
        form = ProviderForm()
    return render(request, '../templates/provider/create_provider.html', {'form': form})


def show(request):
    providers = Provider.objects.all()
    return render(request, '../templates/provider/list_providers.html', {'providers': providers})


def edit(request, id):
    provider = Provider.objects.get(id=id)
    return render(request, '../templates/provider/edit_provider.html', {'provider': provider})


def update(request, id):
    provider = Provider.objects.get(id=id)
    form = ProviderForm(request.POST, instance=provider)
    if form.is_valid():
        form.save()
        return redirect('/provider/list/providers/')
    return render(request, '../templates/provider/edit_provider.html', {'provider': provider})


def destroy(request, id):
    provider = Provider.objects.get(id=id)
    provider.delete()
    return redirect('/provider/list/providers/')
