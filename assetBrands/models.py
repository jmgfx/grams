from django.db import models


class assetBrand(models.Model):
    name = models.CharField(unique=True, max_length=100)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=300)


    def __str__(self):
        return self.name