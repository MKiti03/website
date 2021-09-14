from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('programs-categories', views.programCategory, name = 'program-category'),
    path('programs-categories/<str:category_url>/', views.singleProgramCategory, name = 'single-category'),

    path('all-programs', views.programPage, name='programs'),
    path('<str:program_url>/', views.singleProgram, name='single-program'),
    
    path('all-countries', views.countryPage, name='countries'),
    path('single-country', views.singleCountry, name='single-country'),

    path('universties', views.universityPage, name='universitis'),
    path('single-universty', views.singleUniversity, name='signle-university'),

    path('all-posts', views.blogPostPage, name='post'),
    path('single-post', views.singlePost, name='single-post'),
]