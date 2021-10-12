from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from fontawesome_5.fields import IconField
from osm_field.fields import LatitudeField, LongitudeField, OSMField

# Create your models here.

class BasePage(models.Model):
    page_name = models.CharField(max_length=254, blank=True, null= True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)
    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.page_name

    class Meta:
        verbose_name = 'Base page'
        verbose_name_plural = 'Base pages'

def get_continent():
    return BasePage.objects.get(id = 2)
class Country(models.Model):
    base_page = models.ForeignKey(BasePage, null=True, blank=True, on_delete=models.PROTECT, default=get_continent)
    country_name = models.CharField(max_length=254, null=True, blank=True)
    map_latitud = models.IntegerField(null=True, blank=True)
    map_longitud = models.IntegerField(null=True, blank=True)
    country_flag = models.ImageField(default = 'default.png', blank=True, upload_to = 'countries-flags/%Y/%m/%d/')
    country_image = models.ImageField(default = 'default.png', blank=True, upload_to = 'countries-images/%Y/%m/%d/')
    country_description = RichTextField(null = True, blank = True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)
    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class CountryFact(models.Model):
    fact_name = models.CharField(max_length=254, null=True, blank=True)
    chose_country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=True)
    fact_description = models.TextField(max_length=254, null=True, blank=True)
    fact_icon =IconField(null = True, blank =True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.fact_name

    class Meta:
        verbose_name = 'Country fact'
        verbose_name_plural = 'Countries Fact'
class DiciplineTag(models.Model):
    name = models.CharField(max_length=254, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)
    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dicipline tag'
        verbose_name_plural = 'Dicipline tags'

def get_dicipline():
    return BasePage.objects.get(id = 1)
class Dicipline(models.Model):
    base_page = models.ForeignKey(BasePage, on_delete=models.PROTECT, null=True, blank=True, default=get_dicipline)
    dicipline_name = models.CharField(max_length=254, null=True, blank=True, help_text='Enter the dicipline name :Ex Medecine & Health')
    short_name = models.CharField(max_length=254, null=True, blank = True)
    dicipline_icon = IconField(null = True, blank = True)

    dicipline_image = models.ImageField(default = 'default', blank=True, upload_to = 'dicipline-images/%Y/%m/%d/')

    simple_description = models.TextField(max_length=400, blank=True, null=True, help_text='Simple description for this dicipline in maximum of 500 letters')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)
    set_draft = models.BooleanField(default=True)
    set_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.dicipline_name

    class Meta:
        verbose_name = 'Dicipline'
        verbose_name_plural = 'Diciplines'


def get_specialty():
    return BasePage.objects.get(id = 4)
class Speciality(models.Model):
    base_page = models.ForeignKey(BasePage, on_delete=models.PROTECT, null=True, blank=True, default=get_specialty)
    dicipline = models.ForeignKey(Dicipline, null=True, blank=True, on_delete=models.PROTECT)
    study_level = models.ManyToManyField(DiciplineTag, blank=True,)
    speciality_name = models.CharField(max_length=254, blank=True, null= True)
    speciality_description = RichTextField(null = True, blank=True,)

    year_of_study = models.CharField(max_length=254, blank=True, null=True)
    average_fees = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)
    set_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.speciality_name

    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities' 

def get_university():
    return BasePage.objects.get(id = 3)
class University(models.Model):
    base_page = models.ForeignKey(BasePage, on_delete=models.PROTECT, null=True, blank=True, default=get_university)
    university_name = models.CharField(max_length=254, null=True, blank=True)
    university_specialities = models.ManyToManyField(Speciality, blank=True)
    choose_country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, null=True)
    region = models.CharField(max_length=254, null=True, blank=True)
    university_logo = models.ImageField(default = 'default.png', blank=True, upload_to = 'universities-logo/%Y/%m/%d/')
    university_image = models.ImageField(default = 'default.png', blank=True, upload_to = 'universities-images/%Y/%m/%d/')
    university_description = models.TextField(max_length=700, blank = True, null = True, help_text='Describe this university in maxumun of 700')

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    location = OSMField(null = True, blank = True)
    location_lat = LatitudeField(null = True, blank = True)
    location_lon = LongitudeField(null = True, blank = True)

    def __str__(self):
        return self.university_name

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'
class UniversityFact(models.Model):
    fact_name = models.CharField(max_length=254, null=True, blank=True)
    chose_university = models.ForeignKey(University, on_delete=models.PROTECT, null=True, blank=True)
    fact_description = models.TextField(max_length=254, null=True, blank=True)
    fact_icon = IconField(null = True, blank =True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.fact_name

    class Meta:
        verbose_name = 'University fact'
        verbose_name_plural = 'Universities Fact'

class Program(models.Model):
    program_name = models.CharField(max_length=254, blank=True, null=True)
    study_level = models.ManyToManyField(DiciplineTag)
    program_speciality = models.ForeignKey(Speciality, blank=True, null=True, on_delete=models.PROTECT)
    choose_university = models.ForeignKey(University, blank=True, on_delete=models.PROTECT, null=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)
    set_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.program_name

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

class ProgramFact(models.Model):
    fact_name = models.CharField(max_length=254, null=True, blank=True)
    chose_program = models.ForeignKey(Program, on_delete=models.PROTECT, null=True, blank=True)
    fact_description = models.TextField(max_length=40, null=True, blank=True)
    fact_icon = IconField(null = True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.fact_name

    class Meta:
        verbose_name = 'Program fact'
        verbose_name_plural = 'Programs Fact'

class ContactUs(models.Model):
    full_name = models.CharField(max_length=254, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone_number = models.CharField(max_length=254, blank=True, null=True)
    object = models.CharField(max_length=254, blank=True, null=True)
    message = models.TextField(max_length= 254, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Contact us form'
        verbose_name_plural = 'Contact us forms'