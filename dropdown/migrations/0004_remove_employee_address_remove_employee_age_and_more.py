# Generated by Django 4.1.7 on 2023-07-04 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dropdown', '0003_alter_department_options_alter_employee_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='age',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='contactno',
        ),
    ]