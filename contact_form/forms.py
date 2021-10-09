from django import forms
from django.forms import ModelForm
from django import forms
from .models import Application

class ApplyForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))
    nationality = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    actual_country = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    region = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    year_of_graduation = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    school = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    educational_qualification = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows': 4,
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows': 4,
    }))
    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['level','specialty', 'program', 'university','date_created']