# Generated by Django 4.2.2 on 2023-07-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementcenter', '0002_alter_employee_info_resigndate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_info',
            name='birthday',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='createby',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='employeename',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='hiredate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='idcard',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='sex',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
