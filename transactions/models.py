from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from assets.models import Assets
from branch.models import Branch
from vendors.models import Vendors


class Transactions(models.Model):
    TRANSACTION_TYPE = (
        ('1', 'Maintenance'),
        ('2', 'Transfer'),
        ('3', 'Dispose'),
        ('4', 'Recover'),
    )

    TRANSACTION_STATUS = (
        ('1', 'Queued'),
        ('2', 'Finished'),
        ('3', 'Past Due'),
    )

    date_added = models.DateTimeField(auto_now_add=True)
    ttype = models.CharField(max_length=3, choices=TRANSACTION_TYPE, blank=False, null=False)
    status = models.CharField(max_length=3, choices=TRANSACTION_STATUS, blank=False)
    description = models.TextField(max_length=300, default='None')
    assets_transact = models.ManyToManyField(
        Assets,
        related_name='assets_transactions',
        limit_choices_to={'display':1},
    )
    archived_assets = models.ManyToManyField(
        Assets,
        related_name= 'archived_assets',
        limit_choices_to={'display':0},
    )
    
    # Type 1, Maintenance
    start_date = models.DateField(default=timezone.now, null=False)
    end_date = models.DateField(default=timezone.now, null=False)
    vendor = models.ForeignKey(
        Vendors, 
        blank=True, null=True, on_delete=models.SET_NULL
    )

    # Type 2, Transfer
    branch_destination = models.ForeignKey(
        Branch,
        related_name='destination', null=True,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return str(self.ttype)