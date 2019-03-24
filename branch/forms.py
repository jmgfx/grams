from django.forms import ModelForm, Textarea
from .models import Branch


class AddBranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = ['code', 'name', 'location', 'company']

        widgets = {
            'location': Textarea(attrs={
                'rows': 5,
            }),
        }


class EditBranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'location', 'company']

        widgets = {
            'location': Textarea(attrs={
                'rows': 5,
            }),
        }