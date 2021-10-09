from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from contact_form.forms import ApplyForm
from main.models import Dicipline, Program
from django.contrib import messages

from .models import Application, GetIntouch


# Create your views here.
def getInTouch(request):

    # To display items in nav bar and Category page
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)

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
        'dicipline_to_navebar' :dicipline_to_navebar,
        'program_qs' :program_qs,
    }
    return render(request, 'contact_form/main-page.html', context)



def application(request, program_url):
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)
    application_form = Program.objects.get(id = program_url)

    # print(get_program.study_level.name)
    # init_level = []

    # study_level = init_level.append(get_program.study_level.name)
    
    for item in application_form.study_level.all():
        study_level =item.name


    form = ApplyForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form_instance =form.save(commit=False)
            form_instance.program = application_form
            form_instance.specialty = application_form.program_speciality.speciality_name
            form_instance.university = application_form.choose_university.university_name
            form_instance.level = study_level
            form_instance.save()

            messages.success(request, 'Your application has been submited. We will get back to you as soon as possible')
            return redirect('success')

    context = {
        'form':form,
        'application_form':application_form,
        'dicipline_to_navebar' :dicipline_to_navebar,
    }

    return render(request, 'contact_form/program-apply.html', context)