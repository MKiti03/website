from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


   
    path('articles/<str:article>/', views.articlePage, name = 'article'),

    path('articles/Diciplines/<str:dicipline_url>/', views.singleDicipline, name = 'single-dicipline'),
    path('articles/Universities/<str:university_url>/', views.singleUniversity, name = 'single-university'),
    path('articles/Diciplines/Specialties/<str:speciality_url>/', views.singleSpeciality, name = 'single-speciality'),
    path('articles/Continents/<str:country_url>/', views.singleCountry, name='single-country'),

    # path('programs', views.programPage, name='programs'),
    # path('programs/<str:program_url>/', views.singleProgram, name='single-program'),
    
    path("contact-us/", views.contactUsPage, name="contact"),
    path("about-us/", views.aboutUsPage, name="about"),

    path('success/', views.successPage, name='success')

]