from django.forms import ModelForm
from .models import *

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_description']