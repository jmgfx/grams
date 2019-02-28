"""from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from assets.models import Assets
from branch.models import Branch
from vendors.models import Vendors


class Transactions(models.Model):
    TRANSACTION_TYPE = (
        ('1', 'Maintenance'),
        ('2', 'Transfer'),
        ('3', 'Recover'),
    )

    TRANSACTION_STATUS = (
        ('1', 'Queued'),
        ('2', 'Finished'),
        ('3', 'Past Due'),
    )

    date_added = models.DateTimeField(auto_now_add=True)
    ttype = models.CharField(max_length=3, choices=TRANSACTION_TYPE, blank=False, null=False)
    status = models.CharField(max_length=3, choices=TRANSACTION_STATUS, blank=False)
    description = models.TextField(max_length=300)
    assets_transact = models.ManyToManyField(
        Assets,
        on_delete=models.CASCADE
    )
    
    # Type 1, Maintenance
    schedule = models.DateTimeField(default=timezone.now)
    vendor = models.ForeignKey(
        Vendors, 
        blank=True, null=True, on_delete=models.SET_NULL
    )

    # Type 2, Transfer
    branch_origin = models.ForeignKey(
        Branch,
        related_name='origin',
        on_delete=models.CASCADE
    )
    branch_destination = models.ForeignKey(
        Branch,
        related_name='destination',
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.id
    
"""