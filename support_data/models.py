import datetime

from django.db import models

from hr_system.constants import YES_OR_NO_TYPES
from .constants import  TAX_YEAR_CHOICES


class Country(models.Model):
    """docstring for Countries"""
    country_name = models.CharField(max_length=36)
    country_code = models.CharField(max_length=3)

    def __str__(self):
        return self.country_name


class Nationality(models.Model):
    """docstring for Nationality"""
    country = models.OneToOneField(Country, on_delete=models.CASCADE, primary_key=True)
    country_nationality = models.CharField(max_length=36)

    def __str__(self):
        return self.country_nationality


class DutyStation(models.Model):
    """docstring for DutyStation"""
    duty_station = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.duty_station


class Department(models.Model):
    """docstring for Department"""
    department = models.CharField(max_length=30)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.department


class JobTitle(models.Model):
    """docstring for JobTitle"""
    job_title = models.CharField(max_length=200)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.job_title


class ContractType(models.Model):
    """docstring for ContractType"""
    contract_type = models.CharField(max_length=150)
    contract_expiry = models.IntegerField()
    leave_entitled = models.CharField(max_length=3, choices=YES_OR_NO_TYPES)
    leave_days_entitled = models.IntegerField()

    def __str__(self):
        return self.contract_type


class Relationship(models.Model):
    """docstring for Relationship"""
    relationship = models.CharField(max_length=150)

    def __str__(self):
        return self.relationship


class Organization(models.Model):
    """docstring for Organization"""
    name = models.CharField(max_length=100)
    country = models.OneToOneField(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Grade(models.Model):
    """docstring for Grade"""
    grade = models.CharField(max_length=100)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.grade


class Tax(models.Model):
    """docstring for Taxes"""
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    lower_boundary = models.DecimalField(max_digits=7, decimal_places=2)
    upper_boundary = models.DecimalField(max_digits=7, decimal_places=2)
    fixed_amount = models.DecimalField(max_digits=7, decimal_places=2)
    year = models.IntegerField(choices=TAX_YEAR_CHOICES,  default=datetime.datetime.now().year)

    def __str__(self):
        return self.country


