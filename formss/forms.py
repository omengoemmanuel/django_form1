from django import forms
from django.forms import ModelForm
from .models import Employee, form_two


class EmployeeForm(forms.Form):
    emp_name = forms.CharField(label='Name')
    emp_salary = forms.IntegerField(label='Salary')


class form_twoForm(ModelForm):
    class Meta:
        model = form_two
        fields = ('First_Name', 'Last_Name', 'Index_No', 'gender')

        widgets = {
            'First_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Last_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Index_No': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }
