from .models import Receipt,Profile,Post,Request
from django import forms

class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user_name']

class NewReceiptForm(forms.ModelForm):
    class Meta:
        model=Receipt
        exclude=['profile']

class NewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['name']

class NewRequestForm(forms.ModelForm):
    class Meta:
        model=Request
        exclude=['upload_time']
