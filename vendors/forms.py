from django.forms import ModelForm, Textarea
from .models import Vendors


class AddVendorForm(ModelForm):
    class Meta:
        model = Vendors
        fields = ['name', 'address', 'contact_number', 'contact_email']

        widgets = {
            'address': Textarea(attrs={
                'rows':5,
            })
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