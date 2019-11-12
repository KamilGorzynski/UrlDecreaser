from django.forms import ModelForm
from .models import UrlObject


class UrlObjectForm(ModelForm):
    class Meta:
        model = UrlObject
        fields = ['link']
