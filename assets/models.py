from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator 
from django.contrib.auth.models import User

from assetBrands.models import assetBrand
from assetCategories.models import assetCategory
from branch.models import Branch
from vendors.models import Vendors


class Assets(models.Model):

    IU = 'In Use'
    IS = 'In Storage'
    IM = 'In Maintenance'
    DF = 'Defective'
    AR = 'Archived'

    ASSET_STATUS = (
        (IU, 'Use'),
        (IS, 'Storage'),
        (IM, 'Maintenance'),
        (DF, 'Defective'),
        (AR, 'Archived'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=100, choices=ASSET_STATUS, blank=False)
    date_added = models.DateField(auto_now_add=True)
    date_acquired = models.DateField(default=timezone.now)
    end_of_warranty = models.DateField(default=timezone.now)
    model_no = models.CharField(max_length=100)
    specifications = models.TextField(max_length=240, default='')
    serial_no = models.CharField(max_length=100, unique=True)
    acquisition_cost = models.FloatField(default=0.00, validators=[
        MinValueValidator(0.00),
    ])
    project_life = models.IntegerField(default=12, validators=[
        MinValueValidator(1)
    ])
    dep_value = models.FloatField(default=0.00)
    accrued = models.FloatField(null=True)
    balance = models.FloatField(default=0.00)
    salvage_value = models.FloatField(null=True, validators=[
        MinValueValidator(0.00)
    ])
    book_value = models.FloatField(null=True)

    brand = models.ForeignKey(
        assetBrand,
        null=True,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        assetCategory, 
        null=True,
        on_delete=models.SET_NULL
    )
    vendor = models.ForeignKey(
        Vendors,
        null=True,
        on_delete=models.SET_NULL
    )
    branch = models.ForeignKey(
        Branch, 
        null=True,
        on_delete=models.SET_NULL
    )
    created_by = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )

    it_dep_value = ArrayField(models.FloatField(), null=True)
    it_dep_date = ArrayField(models.DateField(), null=True)
    it_accrued = ArrayField(models.FloatField(), null=True)
    it_balance = ArrayField(models.FloatField(), null=True)

    display = models.CharField(max_length=1, null=False, default=1)
    counter = models.CharField(max_length=3, null=False, default=0)
    depreciate = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name + ' ID#' + str(self.id)

    
    class Meta:
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'