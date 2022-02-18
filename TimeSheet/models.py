from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    deleted_date = models.DateField(null=True)
    deleted_by = models.CharField(null=True, max_length=30)


class WorkDay(models.Model):
    workdate = models.DateField()
    location = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField()
    report_date = models.DateField()
    FBP_billing = 'FBP'
    AMCO_billing = 'AMCO'
    billing_choices = [
        (FBP_billing, 'FBP Billing'),
        (AMCO_billing, 'AMCO Billing'),
    ]
    batch_ID = models.CharField(max_length=100)
    company_code = models.CharField(max_length=100)