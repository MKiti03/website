from django.contrib import admin
from .models import *

# Register your models here.

class BasePageAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'date_created','set_draft', 'last_update')
    list_filter = ("page_name", 'set_draft', 'date_created')
    search_fields = ['page_name']

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('university_name', 'choose_country', 'date_created','set_draft', 'last_update')
    list_filter = ("university_name", 'choose_country', 'set_draft', 'date_created')
    search_fields = ['title', 'content']


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'date_created')
    list_filter = ("full_name", 'date_created')
    search_fields = ['full_name', 'object']


class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_flag', 'date_created', 'set_draft')
    list_filter = ('country_name', 'date_created')
    search_fields = ['country_name', 'set_draft']

class CountryFactAdmin(admin.ModelAdmin):
    list_display = ('fact_name', 'chose_country', 'date_created', 'set_draft')
    list_filter = ('fact_name','chose_country', 'set_draft', 'date_created')
    search_fields = ['fact_name', 'set_draft']

class UniversityFactAdmin(admin.ModelAdmin):
    list_display = ('fact_name', 'chose_university', 'date_created', 'set_draft')
    list_filter = ('fact_name','chose_university', 'set_draft', 'date_created')
    search_fields = ['fact_name', 'set_draft']

class ProgramFactAdmin(admin.ModelAdmin):
    list_display = ('fact_name', 'chose_program', 'date_created', 'set_draft')
    list_filter = ('fact_name','chose_program', 'set_draft', 'date_created')
    search_fields = ['fact_name', 'set_draft']


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('speciality_name', 'date_created', 'last_update', 'set_draft')
    list_filter = ('speciality_name', 'set_draft', 'date_created')
    search_fields = ['speciality_name', 'set_draft']

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'choose_university', 'date_created', 'set_draft', 'set_featured')
    list_filter = ('program_name', 'set_featured', 'set_draft', 'date_created')
    search_fields = ['program_name', 'program_category' 'set_draft', 'set_featured']

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post_category_title', 'date_created', 'set_draft')
    list_filter = ('post_category_title', 'date_created', 'set_draft')

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'date_created', 'set_featured', 'set_draft')
    list_filter = ('post_title', 'post_category', 'set_draft', 'date_created', 'set_featured')

admin.site.register(BasePage, BasePageAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(UniversityFact, UniversityFactAdmin)
admin.site.register(CountryFact, CountryFactAdmin)
admin.site.register(ProgramFact, ProgramFactAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Dicipline)
admin.site.register(DiciplineTag)