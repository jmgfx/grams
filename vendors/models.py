from django.db import models

class Vendors(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.TextField(max_length=500, blank=False, null=False)
    contact_number = models.CharField(max_length=100, default='None')
    contact_email = models.CharField(max_length=100, default='None')
