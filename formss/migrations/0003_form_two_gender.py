# Generated by Django 3.2.24 on 2024-10-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formss', '0002_form_two'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_two',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('Female', 'Female')], default='select gender', max_length=10),
        ),
    ]