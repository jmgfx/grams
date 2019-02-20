from django.forms import ModelForm
from .models import assetCategory


class AddAssetCategory(ModelForm):
    class Meta:
        model = assetCategory
        fields = ['name']