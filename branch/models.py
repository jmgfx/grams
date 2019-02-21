from django.db import models
from django.contrib.auth.models import User
from company.models import Company


class Branch(models.Model):
    code = models.CharField(unique=True, max_length=5)
    name = models.CharField(unique=True, max_length=100 )
    location = models.TextField()
    company = models.ForeignKey(
        Company, null=False, default='None',
        on_delete=models.CASCADE
    )
    """owners = models.ForeignKey(
        User, null=True, on_delete=SET_NULL
    )"""


    def __str__(self):
        return self.name