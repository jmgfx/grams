from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    owners = models.ManyToManyField(
        User,
        related_name='owners',
    )
    date_added = models.DateField(auto_now_add=True)

    # Circular import issue -- use appname.ClassName as a string for workaround
    # Reverse query name issue -- add related_name for workaround
    branches = models.ForeignKey(
        'branch.Branch',
        related_name='children',
        blank=True, null=True, on_delete=models.SET_NULL
    )
    created_by = models.ForeignKey(
        User,
        related_name='created_by',
        blank=True, null=True, on_delete=models.SET_NULL,
    )

    display = models.CharField(max_length=1, default=1)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        