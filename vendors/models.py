from django.db import models
from django.contrib.auth.models import User

from assetCategories.models import assetCategory


class Vendors(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)
    date_added = models.DateField(auto_now_add=True)
    address = models.TextField(max_length=500, blank=False, null=False)
    contact_number = models.CharField(max_length=100, default='None')
    contact_email = models.CharField(max_length=100, default='None')

    category = models.ForeignKey(
        assetCategory,
        on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
    )

    display = models.CharField(max_length=1, default=1)


    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'
        