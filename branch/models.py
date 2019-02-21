"""from django.db import models
from django.contrib.auth.models import User
from company.models import Company


class Branch(models.Model):
    code = models.CharField(unique=True, max_lenght=100)
    name = models.TextField(unique=True)
    location = models.TextField()
    owners = models.ForeignKey(
        User, null=True, on_delete=SET_NULL
    )
    """