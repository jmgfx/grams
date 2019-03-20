import datetime
from django import forms
from django.forms import ModelForm, Form
from .models import Assets


class AddAssetForm(ModelForm):
    class Meta:
        model = Assets

        fields = ['name', 
                'quantity', 
                'status', 
                'date_acquired', 
                'end_of_warranty', 
                'brand', 
                'category', 
                'branch',
                'model_no', 
                'serial_no', 
                'specifications',
                'acquisition_cost', 
                'project_life', 
                'salvage_value',
                'description']

        widgets = {
            'date_acquired': forms.SelectDateWidget(years=range(2000, 2030)),
            'end_of_warranty': forms.SelectDateWidget,
        }


class EditAssetForm(ModelForm):
    class Meta:
        model = Assets

        fields = ['name', 
                'quantity',
                'end_of_warranty', 
                'specifications',
                'brand', 
                'category',
                'description']

        widgets = {
            'end_of_warranty': forms.SelectDateWidget,
        }


class RevalueForm(ModelForm):
    class Meta:
        model = Assets
        
        fields = ['acquisition_cost', 
                'project_life', 
                'salvage_value']
