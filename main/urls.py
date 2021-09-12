from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single-program', views.singleProgram, name='single-program'),
    path('all-programs', views.programPage, name='programs'),
    path('universties', views.universityPage, name='universitis'),
    path('single-universty', views.singleUniversity, name='signle-university'),
    path('all-countries', views.countryPage, name='countries'),
    path('single-country', views.singleCountry, name='single-country'),
]