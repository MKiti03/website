from django.contrib import admin
from .models import *

# Register your models here.
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('university_name', 'chose_country', 'date_created','set_draft', 'last_update')
    list_filter = ("university_name", 'chose_country', 'set_draft', 'date_created')
    search_fields = ['title', 'content']


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'date_created')
    list_filter = ("full_name", 'date_created')
    search_fields = ['full_name', 'object']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_account', 'user_phone_number', 'date_created')
    list_filter = ('user_account', 'user_phone_number', 'date_created')
    search_fields = ['user_account','user_account']

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


class ProgramCategoryAdmin(admin.ModelAdmin):
    list_display = ('program_category_title', 'date_created', 'last_update', 'set_draft')
    list_filter = ('program_category_title', 'set_draft', 'date_created')
    search_fields = ['program_category_title', 'set_draft']

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'program_category', 'choose_university', 'date_created', 'set_draft', 'set_featured')
    list_filter = ('program_name', 'program_category', 'set_featured', 'set_draft', 'date_created')
    search_fields = ['program_name', 'program_category' 'set_draft', 'set_featured']

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post_category_title', 'date_created', 'set_draft')
    list_filter = ('post_category_title', 'date_created', 'set_draft')

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'date_created', 'set_featured', 'set_draft')
    list_filter = ('post_title', 'post_category', 'set_draft', 'date_created', 'set_featured')


admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UniversityFact, UniversityFactAdmin)
admin.site.register(CountryFact, CountryFactAdmin)
admin.site.register(ProgramFact, ProgramFactAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(ProgramCategory, ProgramCategoryAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(PostComment)
admin.site.register(Tag)
admin.site.register(Country, CountryAdmin)
admin.site.register(TeamMember)
admin.site.register(TeamMemberSkill)
admin.site.register(InterpriseContactInformatiom)