from django.contrib import admin
from .models import *

# Register your models here.
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('university_name', 'chose_country', 'date_created','set_draft', 'last_update')
    list_filter = ("university_name",)
    search_fields = ['title', 'content']




admin.site.register(ContactUs)
admin.site.register(UserProfile)
admin.site.register(UniversityFact)
admin.site.register(CountryFact)
admin.site.register(ProgramFact)
admin.site.register(University, UniversityAdmin)
admin.site.register(ProgramCategory)
admin.site.register(Program)
admin.site.register(BlogPost)
admin.site.register(PostCategory)
admin.site.register(PostComment)
admin.site.register(Tag)
admin.site.register(Country)
admin.site.register(TeamMember)
admin.site.register(TeamMemberSkill)
admin.site.register(InterpriseContactInformatiom)