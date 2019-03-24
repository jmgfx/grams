from django.forms import ModelForm, Textarea
from .models import assetBrand


class AddAssetBrand(ModelForm):
    class Meta:
        model = assetBrand
        fields = ['name', 'description']

        widgets = {
            'description': Textarea(attrs={
                'rows': 5,
            }),
        }


class EditAssetBrand(ModelForm):
    class Meta:
        model = assetBrand
        fields = ['name', 'description']

        widgets = {
            'description': Textarea(attrs={
                'rows': 5,
            }),
        }