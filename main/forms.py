from django.forms import ModelForm
from .models import *

class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        exclude = ['date_created']