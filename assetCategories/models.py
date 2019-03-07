from django.db import models
from django.utils import timezone


class assetCategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=300, null=True)
    

    def __str__(self):
        return self.name