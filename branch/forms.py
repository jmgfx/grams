from django.forms import ModelForm
from .models import Branch


class AddBranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = ['code', 'name', 'location', 'company']