from main.forms import UserProfileForm
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def index(request):

    # form = UserProfileForm()

    # if request.method == 'POST':
    #     user = request.user
    #     profile_description = request.POST.get('profile_description')

    #     if USerProfile.objects.filter(user_account = user).exists():

    #         user_profile = USerProfile.objects.filter(user_account = user)

    #         user_profile.update(profile_description =profile_description)


    # context = {
    #     'form':form,
    # }
    return render(request, 'main/main-home-page.html')

def programPage(request):

    return render(request, 'main/program.html')

def singleProgram(request):

    return render(request, 'main/single-program.html')

def universityPage(request):

    return render(request, 'main/university.html')

def singleUniversity(request):
    return render(request, 'main/single-university.html')

def countryPage(request):
    return render(request, 'main/countries.html')

def singleCountry(request):
    return render(request, 'main/single-country.html')