from django.forms import ModelForm
from .models import assetBrand


class AddAssetBrand(ModelForm):
    class Meta:
        model = assetBrand
        fields = ['name']