# Generated by Django 2.2b1 on 2019-03-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payrollperiod',
            name='payroll_key',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]