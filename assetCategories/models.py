from django.db import models


class assetCategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    

    def __str__(self):
        return self.name