from django import forms
from django.forms import ModelForm
from .models import *

class ContactForm(ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))
    object = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'

    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows': 4,
    }))
    class Meta:
        model = ContactUs
        fields = ['full_name', 'phone_number', 'email', 'object', 'message']