from django.db import models

from main.models import Program

# Create your models he
class GetIntouch(models.Model):
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    nationality = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=254, null=True, blank=True)
    graduation_year = models.DateField(null=True, blank=True)
    program_cateory = models.CharField(max_length=254, null=True, blank=True)
    course_of_interest = models.CharField(max_length=254, null=True, blank=True)
    educational_qualification = models.TextField(max_length=254, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
        verbose_name = 'Get in touch'
        verbose_name_plural = 'Get in touchs'

class Application(models.Model):
    program = models.ForeignKey(Program, null=True, blank=True, on_delete=models.PROTECT)
    university = models.CharField(max_length=254, null=True, blank=True)
    specialty = models.CharField(max_length=254, null=True, blank=True)
    level = models.CharField(max_length=254, null=True, blank=True)

    name = models.CharField(max_length=254, null=True, blank=True, help_text='Your Name')
    phone = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    
    nationality = models.CharField(max_length=254, null=True, blank=True)
    actual_country = models.CharField(max_length=254, null=True, blank=True)
    region = models.CharField(max_length=254, null=True, blank=True)
    address = models.CharField(max_length=254, null=True, blank=True)

    year_of_graduation = models.DateField( auto_now_add=False, null=True, blank=True)
    school = models.CharField(max_length=254, null=True, blank=True)
    educational_qualification = models.TextField(max_length=254, null=True, blank=True)

    message = models.TextField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'