from django.urls import path

from formss import views

urlpatterns = [
    path('', views.employee_data, name='employee_data'),
    path('employee_submit/', views.employee_submit, name='employee_submit'),
    path('form__two', views.form__two, name='form__two'),
    path('form_two_sub/', views.form_two_sub, name='form_two_sub')
]
