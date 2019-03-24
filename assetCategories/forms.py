from django.forms import ModelForm, Textarea
from .models import assetCategory


class AddAssetCategory(ModelForm):
    class Meta:
        model = assetCategory
        fields = ['name', 'description']

        widgets = {
            'description': Textarea(attrs={
                'rows': 5,
            }),
        }


class EditAssetCategory(ModelForm):
    class Meta:
        model = assetCategory
        fields = ['name', 'description']

        widgets = {
            'description': Textarea(attrs={
                'rows': 5,
            }),
        }