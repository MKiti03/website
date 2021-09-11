from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single-program', views.singleProgram, name='single-program'),
    path('universties', views.universityPage, name='universitis'),
]