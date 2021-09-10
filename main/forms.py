from django.forms import ModelForm
from .models import *

class UserProfileForm(ModelForm):
    class Meta:
        model = USerProfile
        fields = ['profile_description']