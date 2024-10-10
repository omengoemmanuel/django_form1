from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EmployeeForm, form_twoForm
from .models import Employee, form_two


# Create your views here.
def employee_data(request):
    form = EmployeeForm()
    return render(request, 'employee.html', {'form': form})


def employee_submit(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp_name = form.cleaned_data['emp_name']
            emp_salary = form.cleaned_data['emp_salary']

            employ = Employee.objects.create(emp_name=emp_name, emp_salary=emp_salary)
            employ.save()
            messages.success(request, "Save successfully")
            return redirect('employee_data')


def form__two(request):
    model = form_two
    form = form_twoForm()
    return render(request, 'form_two.html', {'form': form})


def form_two_sub(request):
    if request.method == 'POST':
        form = form_twoForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('form__two')
