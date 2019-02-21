from django.db import models
from django.contrib.auth.models import User
"""from branch.models import Branch"""


class Company(models.Model):
    name = models.CharField(max_length=100)
    owners = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL
    )
    """
    branches = models.ManyToManyField(ForeignKey(
        Branch, 
        choices = Branch.code.all(),
        blank=True, null=True, on_delete=SET_NULL
    ))"""


    def __str__(self):
        return self.name