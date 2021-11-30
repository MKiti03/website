from django.urls import path
from .views import *

urlpatterns = [
    path('', getInTouch, name='get-in-touch'),

    path('universities/apply/<str:program_url>/', application, name='application'),

    path('email-template', testEmailTemplete, name='email'),

    path('quick-apply', quickApply, name='quick-apply'),
    path('get-dicipline', getDicipline, name='get-dicipline'),
    path('get-specialty', getSpecialty, name='get-specialty'),
]