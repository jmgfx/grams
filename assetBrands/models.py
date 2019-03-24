from django.db import models
from django.contrib.auth.models import User


class assetBrand(models.Model):
    name = models.CharField(unique=True, max_length=100)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=300)

    created_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Asset Brand'
        verbose_name_plural = 'Asset Brands'