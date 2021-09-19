from django.db import models

# Create your models he
class GetIntouch(models.Model):
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_mame = models.CharField(max_length=254, null=True, blank=True)
    nationality = models.CharField(max_length=254, null=True, blank=True)
    emial = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=254, null=True, blank=True)
    graduation_year = models.DateField(null=True, blank=True)
    course_of_interest = models.CharField(max_length=254, null=True, blank=True)
    educational_qualification = models.CharField(max_length=254, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.first_name + self.last_mame

    class Meta:
        verbose_name = 'Get in touch'
        verbose_name_plural = 'Get in touchs'

class ContactUs(models.Model):
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_mame = models.CharField(max_length=254, null=True, blank=True)
    nationality = models.CharField(max_length=254, null=True, blank=True)
    country_of_residence = models.CharField(max_length=254, null=True, blank=True)
    emial = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=254, null=True, blank=True)
    graduation_year = models.DateField(null=True, blank=True)
    course_of_interest = models.CharField(max_length=254, null=True, blank=True)
    educational_qualification = models.CharField(max_length=254, null=True, blank=True)
    additinal_infoemation = models.TextField(max_length= 254, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Contact us form'
        verbose_name_plural = 'Contact us forms'

    