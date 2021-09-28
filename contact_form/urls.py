from django.urls import path
from .views import *

urlpatterns = [
    path('', getInTouch, name='get-in-touch'),
]