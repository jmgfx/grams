from django.db import models
from django.contrib.auth.models import User
from company.models import Company


class Branch(models.Model):
    code = models.CharField(unique=True, max_length=5)
    name = models.CharField(unique=True, max_length=100 )
    date_added = models.DateField(auto_now_add=True)
    location = models.TextField()
    company = models.ForeignKey(
        Company,
        null=True,
        on_delete=models.SET_NULL
    )
    created_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
    )

    display = models.CharField(max_length=1, default=1)


    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'