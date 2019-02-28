from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from assetBrands.models import assetBrand
from assetCategories.models import assetCategory
from branch.models import Branch

class Assets(models.Model):

    IU = 'In Use'
    IS = 'In Storage'
    IM = 'In Maintenance'
    DF = 'Defective'
    AR = 'Archived'

    ASSET_STATUS = (
        ('In Use', 'In Use'),
        ('In Storage', 'In Storage'),
        ('In Maintenance', 'In Maintenance'),
        ('Defective', 'Defective'),
        ('Archived', 'Archived'),
    )

    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default='1')
    description = models.TextField(max_length=300)
    status = models.CharField(max_length=100, choices=ASSET_STATUS, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_acquired = models.DateTimeField(default=timezone.now)
    end_of_warranty = models.DateTimeField(default=timezone.now)
    model_no = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)
    acquisition_cost = models.FloatField()
    projected_life = models.DurationField()
    accrued = models.FloatField(null=True)
    balance = models.FloatField(null=True)
    salvage_value = models.FloatField(null=True)
    book_value = models.FloatField(null=True)

    brand = models.ForeignKey(
        assetBrand,
        blank=True, null=True, on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        assetCategory, 
        blank=True, null=True, on_delete=models.SET_NULL
    )
    branch = models.ForeignKey(
        Branch, 
        blank=True, null=True, on_delete=models.SET_NULL
    )
    

    def __str__(self):
        return self.name
