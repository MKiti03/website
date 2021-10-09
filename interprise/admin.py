from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

# Model admin registration
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_account', 'user_phone_number', 'date_created')
    list_filter = ('user_account', 'user_phone_number', 'date_created')
    search_fields = ['user_account','user_account']

    
# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(TeamMember)
admin.site.register(TeamMemberSkill)
admin.site.register(InterpriseContactInformatiom)