from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from fontawesome_5.fields import IconField
from osm_field.fields import LatitudeField, LongitudeField, OSMField


# Create your models here.
class UserProfile(models.Model):
    user_account = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    user_phone_number = models.CharField(max_length=254, null=True, blank=True)
    user_address = models.CharField(max_length=254, null = True, blank=True)

    profile_description = RichTextField(null = True, blank = True)

    user_profile_pic = models.ImageField(default = 'default.png', blank=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user_account)

    class Meta:
        verbose_name = 'User Account'
        verbose_name_plural = 'Users Accounts'
        
class TeamMember(models.Model):
    name = models.CharField(max_length=254, null =True, blank=True)
    role = models.CharField(max_length=254, null=True, blank=True)
    profile_image = models.ImageField(default = 'default.png', upload_to = 'testimonials-images/%Y/%m/%d/', blank=True)

    phone_number = models.CharField(max_length=254, null=True,blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    address = models.CharField(max_length=254, null = True, blank=True)

    team_membre_description = RichTextField(null = True, blank = True)

    facebook_account = models.URLField(max_length=254, null =True, blank=True)
    linkedin_account = models.URLField(max_length=254, null =True, blank=True)
    twiter_account = models.URLField(max_length=254, null =True, blank=True)
    instagram_account = models.URLField(max_length=254, null =True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team member'
        verbose_name_plural = 'Team Members'

class TeamMemberSkill(models.Model):
    skill = models.CharField(max_length=254, null = True, blank=True)
    assign_to = models.OneToOneField(TeamMember, null=True, blank=True, on_delete=models.PROTECT)
    skill_level = models.IntegerField(null=True, blank=True)
    skill_detail = RichTextField(null = True, blank = True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Team member skill'
        verbose_name_plural = 'Team Members skills'
class InterpriseContactInformatiom(models.Model):
    phone_number = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    address = models.CharField(max_length=254, null=True, blank=True)

    facebook_account = models.URLField(max_length=254, null =True, blank=True)
    linkedin_account = models.URLField(max_length=254, null =True, blank=True)
    twiter_account = models.URLField(max_length=254, null =True, blank=True)
    instagram_account = models.URLField(max_length=254, null =True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Interprise contact information'
        verbose_name_plural = 'Interprise contact informations'
