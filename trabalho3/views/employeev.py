from django.shortcuts import render, redirect
from trabalho3.forms.employeef import EmployeeForm
from trabalho3.models.employee import Employee


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/employee/list/employees/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, '../templates/employee/create_employee.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, '../templates/employee/list_employees.html', {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, '../templates/employee/edit_employee.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/employee/list/employees/')
    return render(request, '../templates/employee/edit_employee.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/employee/list/employees/')
