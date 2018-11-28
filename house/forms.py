from .models import Receipt,Profile
from django import forms

class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user_name']

class NewReceiptForm(forms.ModelForm):
    class Meta:
        model=Receipt
        exclude=['profile']
