from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class UserProfile(models.Model):
    user_account = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    user_phone_number = models.CharField(max_length=254, null=True, blank=True)
    user_address = models.CharField(max_length=254, null = True, blank=True)

    profile_description = RichTextField(null = True, blank = True)

    user_profile_pic = models.ImageField(default = 'default.png')

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user_account)

    class Meta:
        verbose_name = 'User Account'
        verbose_name_plural = 'Users Accounts'
class Country(models.Model):
    country_name = models.CharField(max_length=254, null=True, blank=True)
    map_latitud = models.IntegerField(null=True, blank=True)
    map_longitud = models.IntegerField(null=True, blank=True)
    country_image = models.ImageField(default = 'default.png')
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
    chose_country = models.OneToOneField(Country, on_delete=models.PROTECT, null=True, blank=True)
    fact_description = models.TextField(max_length=254, null=True, blank=True)
    fact_icon = models.CharField(max_length=254, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.fact_name

    class Meta:
        verbose_name = 'Country fact'
        verbose_name_plural = 'Countries Fact'
class University(models.Model):
    university_name = models.CharField(max_length=254, null=True, blank=True)
    chose_country = models.OneToOneField(Country, on_delete=models.PROTECT, null=True, blank=True)
    university_image = models.ImageField(default = 'default.png')
    university_description = RichTextField(blank = True, null = True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.university_name

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'
class UniversityFact(models.Model):
    fact_name = models.CharField(max_length=254, null=True, blank=True)
    chose_university = models.OneToOneField(University, on_delete=models.PROTECT, null=True, blank=True)
    fact_description = models.TextField(max_length=254, null=True, blank=True)
    fact_icon = models.CharField(max_length=254, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.fact_name

    class Meta:
        verbose_name = 'University fact'
        verbose_name_plural = 'Universities Fact'
class ProgramCategory(models.Model):
    program_category_title = models.CharField(max_length=254, null= True, blank=True)
    program_category_description = RichTextField(null = True, blank = True)
    program_category_image = models.ImageField(default = 'default')

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.post_category_title

    class Meta:
        verbose_name = 'Program Category'
        verbose_name_plural = 'Program Categories'     

class Program(models.Model):
    program_name = models.CharField(max_length=254, null=True, blank=True)
    program_category = models.ManyToManyField(ProgramCategory, blank=True)
    choose_university = models.OneToOneField(University, on_delete=models.PROTECT, null=True, blank=True)
    program_description = RichTextField(blank = True, null = True)
    program_image = models.ImageField(default = 'default.pmg')

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.program_name

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

class ProgramFact(models.Model):
    fact_name = models.CharField(max_length=254, null=True, blank=True)
    chose_program = models.OneToOneField(Program, on_delete=models.PROTECT, null=True, blank=True)
    fact_description = models.TextField(max_length=254, null=True, blank=True)
    fact_icon = models.CharField(max_length=254, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.fact_name

    class Meta:
        verbose_name = 'Program fact'
        verbose_name_plural = 'Programs Fact'
class PostCategory(models.Model):
    post_category_title = models.CharField(max_length=254, null= True, blank=True)
    post_category_description = RichTextField(null = True, blank = True)
    pOst_category_image = models.ImageField(default = 'default')

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.post_category_title

    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Post Categories'

class Tag(models.Model):
    tag_name = models.CharField(max_length=254, null=True, blank=True)
    
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
class BlogPost(models.Model):
    post_title = models.CharField(max_length=254, null =True, blank=True)
    post_category = models.OneToOneField(PostCategory, on_delete=models.PROTECT, null=True, blank=True)
    post_tag = models.ManyToManyField(Tag, blank=True)
    psot_description = RichTextField(null = True, blank = True)
    post_image = models.ImageField(default = 'default.png')
    

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blogs Post'

class PostComment(models.Model):
    commented_by = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    blog_post = models.OneToOneField(BlogPost, on_delete=models.PROTECT)
    commment = models.TextField(max_length=500, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    set_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.commment

    class Meta:
        verbose_name = 'Post comment'
        verbose_name_plural = 'Post Comments'


class TeamMember(models.Model):
    name = models.CharField(max_length=254, null =True, blank=True)
    role = models.CharField(max_length=254, null=True, blank=True)
    profile_image = models.ImageField(default = 'default.png')

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

