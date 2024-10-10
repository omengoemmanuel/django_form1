from django.db import models


# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=50, null=False, blank=False)
    emp_salary = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.emp_name


class form_two(models.Model):
    First_Name = models.CharField(max_length=20, null=False, blank=False)
    Last_Name = models.CharField(max_length=20, null=False, blank=False)
    Index_No = models.PositiveIntegerField()
    gender_choice = [
        ('male', 'Male'),
        ('Female', 'Female')
    ]
    gender = models.CharField(max_length=10, default="select gender", null=False, blank=False, choices=gender_choice)

    def __str__(self):
        return self.First_Name + self.Last_Name
