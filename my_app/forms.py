from django import forms
from . import models


class CreateItem(forms.ModelForm):
    class Meta:
        model = models.all_items
        fields = ['product_type', 'gender', 'color', 'size', 'description', 'picture']


class SignupInformation(forms.ModelForm):
    class Meta:
        model = models.users
        fields = ['birthday', 'country', 'address', 'email', 'picture']
