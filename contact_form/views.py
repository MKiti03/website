from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from main.models import ProgramCategory, Program
from django.contrib import messages

from .models import GetIntouch


# Create your views here.
def getInTouch(request):

    # To display items in nav bar and Category page
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    # To display items in nav bar and Category page
    program_qs = Program.objects.all().filter(set_draft = False)

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        nationality = request.POST.get('nationality')
        country = request.POST.get('country')
        date = request.POST.get('date')
        program = request.POST.get('program')
        education = request.POST.get('education')

        get_in_touch = GetIntouch.objects.create(
            first_name = first_name,
            last_name = last_name,
            nationality = nationality,
            email = email,
            phone_number = phone,
            country = country,
            graduation_year = date,
            course_of_interest = program,
            educational_qualification = education,
        )

        try:
            get_in_touch.save()
            
            messages.success(request, 'Your request has been submited, we will get back to you as soon as possible')
            return redirect('get-in-touch')
        except:
            messages.info(request, 'An error occurred while sending your request, please try again later')
            return redirect('get-in-touch')

    context = {
        'category_to_navebar' :category_to_navebar,
        'program_qs' :program_qs,
    }
    return render(request, 'contact_form/main-page.html', context)