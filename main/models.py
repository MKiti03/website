from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

from ckeditor.fields import RichTextField

# Create your models here.
class USerProfile(models.Model):
    user_account = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    user_phone_number = models.CharField(max_length=254, null=True, blank=True)
    user_address = models.CharField(max_length=254, null = True, blank=True)

    profile_description = RichTextField(null = True, blank = True)

    user_profile_pic = models.ImageField(default = 'default.png')

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.user_account)

    class Meta:
        verbose_name = 'User Account'
        verbose_name_plural = 'Users Accounts'

class UniversityFact(models.Model):
    fact_name = models.CharField(max_length=254, null=True, blank=True)
    fact_description = models.TextField(max_length=254, null=True, blank=True)
    fact_icon = models.CharField(max_length=254, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.fact_name

    class Meta:
        verbose_name = 'University fact'
        verbose_name_plural = 'Universities Fact'

class University(models.Model):
    university_name = models.CharField(max_length=254, null=True, blank=True)
    university_fact = models.ManyToManyField(UniversityFact, blank=True)
    university_image = models.ImageField(default = 'default.png')
    university_description = RichTextField(blank = True, null = True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.university_name

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'

class Pages(models.Model):
    page_name = models.CharField(max_length=254, null=True, blank=True)
    realted_university = models.ManyToManyField(University, blank=True)
    page_description = RichTextField(blank = True, null = True)
    page_image = models.ImageField(default = 'default.pmg')

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.page_name

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

