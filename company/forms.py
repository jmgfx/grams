from django.forms import ModelForm
from .models import Company


class AddCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'owners']