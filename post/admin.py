from django.contrib import admin


from .models import *

# Register your models here.
admin.site.register(PostCategory)
admin.site.register(BlogPost)
admin.site.register(PostComment)
admin.site.register(Tag)