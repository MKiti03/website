from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from fontawesome_5.fields import IconField
from osm_field.fields import LatitudeField, LongitudeField, OSMField
# Create your models here.


class PostCategory(models.Model):
    post_category_title = models.CharField(max_length=254, null= True, blank=True)
    post_category_description = models.TextField(max_length=254 ,null = True, blank = True)
    post_category_image = models.ImageField(default = 'default', upload_to = 'blog-images/%Y/%m/%d/')

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.post_category_title

    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Post Categories'

class BlogPost(models.Model):
    post_title = models.CharField(max_length=254, null =True, blank=True)
    post_category = models.ManyToManyField(PostCategory, blank=True)
    post_description = RichTextField(null = True, blank = True)
    post_image = models.ImageField(default = 'default.png', upload_to = 'blog-images/%Y/%m/%d/')
    

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)
    set_featured = models.BooleanField(default=True)

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blogs Post'
class Tag(models.Model):
    tag_name = models.CharField(max_length=254, null=True, blank=True)
    post = models.ForeignKey(BlogPost, null=True, blank=True, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
class PostComment(models.Model):
    commented_by = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.PROTECT, null=True, blank=True)
    comment = models.TextField(max_length=500, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.commented_by

    class Meta:
        verbose_name = 'Post comment'
        verbose_name_plural = 'Post Comments'
