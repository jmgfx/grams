from django.forms import ModelForm, Textarea
from .models import Vendors


class AddVendorForm(ModelForm):
    class Meta:
        model = Vendors
        fields = ['name', 'category', 'address', 'contact_number', 'contact_email']

        widgets = {
            'address': Textarea(attrs={
                'rows': 1,
            })
        }

        labels = {
            'name': 'Vendor Name',
            'category': 'Asset Categories',
        }


class EditVendorForm(ModelForm):
    class Meta:
        model = Vendors
        fields = fields = ['name', 'address', 'contact_number', 'contact_email']

        widgets = {
            'address': Textarea(attrs={
                'rows':5,
            })
        }