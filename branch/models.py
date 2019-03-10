from django.db import models
from django.contrib.auth.models import User
from company.models import Company


class Branch(models.Model):
    code = models.CharField(unique=True, max_length=5)
    name = models.CharField(unique=True, max_length=100 )
    date_added = models.DateField(auto_now_add=True)
    location = models.TextField()
    company = models.ForeignKey(
        Company, null=False, default=1,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.name