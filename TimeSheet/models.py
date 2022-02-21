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
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    workdate = models.DateField()
    location = models.CharField(max_length=100)
    sector = models.CharField(max_length=30)
    time_in = models.TimeField()
    time_out = models.TimeField()
    report_date = models.DateField(auto_now_add=True)
    billing = models.CharField(max_length=100)
    batch_ID = models.CharField(max_length=100)
    company_code = models.CharField(max_length=100)

    def save(self, *args, **kwargs):

        east_hospitals = ('h1', 'h2', 'h3')
        west_hospitals = ('h4', 'h5')
        if self.location in east_hospitals:
            self.sector = 'East'
        elif self.location in west_hospitals:
            self.sector = 'West'
        else:
            self.sector = 'No sector associated to selected hospital. Check East/West lists.'

        self.batch_ID = 12001569253
        self.company_code = 'H-9253-2'

        super(WorkDay, self).save(*args, **kwargs)