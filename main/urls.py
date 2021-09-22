from django.urls import path
from . import views

from .views import BlogPostPage

urlpatterns = [
    path('', views.index, name='index'),

    path('programs-categories', views.programCategory, name = 'program-category'),
    path('programs-categories/<str:category_url>/', views.singleProgramCategory, name = 'single-category'),

    path('programs', views.programPage, name='programs'),
    path('programs/<str:program_url>/', views.singleProgram, name='single-program'),
    
    path('countries', views.countryPage, name='countries'),
    path('countries/<str:country_url>/', views.singleCountry, name='single-country'),

    path('universities', views.universityPage, name='universitis'),
    path('universities/<str:university_url>/', views.singleUniversity, name='signle-university'),

    path('posts-categories', views.postCategory, name = 'post-category'),
    path('posts-categories/<str:post_category_url>/', views.singlePostCategory, name = 'single-post-category'),

    path('all-posts', BlogPostPage.as_view(), name= 'post'),
    path('all-posts/<str:single_post_url>/', views.singlePost, name='single-post'),

    path("contact-us/", views.contactUsPage, name="contact"),
    path("about-us/", views.aboutUsPage, name="about"),

    path('success/', views.successPage, name='success')

]