from django.core import mail
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import html
from contact_form.forms import ApplyForm
from main.models import Country, Dicipline, DiciplineTag, Program, Speciality, University, get_specialty
from django.contrib import messages

from .models import Application, GetIntouch
from main.models import BasePage

from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def getInTouch(request):

    # To display items in nav bar and Category page
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)
    
    base_page_continent = None
    base_page_university = None
    base_page_dicipline = None
    try:
        base_page_dicipline = BasePage.objects.get(page_name = 'Diciplines')
        base_page_continent = BasePage.objects.get(page_name = 'Continents')
        base_page_university = BasePage.objects.get(page_name = 'Universities')
    except:
        pass

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

            context = {
                'first_name':first_name,
                'last_name':last_name,
                'nationality':nationality,
                'email':email,
                'phone':phone,
                'country':country,
                'date':date,
                'program':program,
                'education':education,
            }
            mail_template = render_to_string('email_get_in_touch.html', context)
            mail_content = strip_tags(mail_template)

            email_to_send = EmailMultiAlternatives(
                "Study abroad form submited",
                mail_content,
                settings.EMAIL_HOST_USER,
                ['studyabroad@vecademy.com',]
            )

            email_to_send.attach_alternative(
                mail_template,
                "text/html"
            )

            email_to_send.send()
            messages.success(request, 'Your request has been submited, we will get back to you as soon as possible')
            return redirect('get-in-touch')
        except:
            messages.info(request, 'An error occurred while sending your request, please try again later')
            return redirect('get-in-touch')

    context = {
        'base_page_continent':base_page_continent,
        'base_page_university':base_page_university,
        'base_page_dicipline':base_page_dicipline,
        'dicipline_to_navebar' :dicipline_to_navebar,
        'program_qs' :program_qs,
    }
    return render(request, 'contact_form/main-page.html', context)



def application(request, program_url):
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)
    application_form = Program.objects.get(id = program_url)
    
    base_page_continent = None
    base_page_university = None
    base_page_dicipline = None
    try:
        base_page_dicipline = BasePage.objects.get(page_name = 'Diciplines')
        base_page_continent = BasePage.objects.get(page_name = 'Continents')
        base_page_university = BasePage.objects.get(page_name = 'Universities')
    except:
        pass

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
        'base_page_continent':base_page_continent,
        'base_page_university':base_page_university,
        'base_page_dicipline':base_page_dicipline,
        'form':form,
        'application_form':application_form,
        'dicipline_to_navebar' :dicipline_to_navebar,
    }

    return render(request, 'contact_form/program-apply.html', context)

def testEmailTemplete(request):
    return render(request, 'email_get_in_touch.html')

def quickApply(request):
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)
    country_to_form = Country.objects.all().filter(set_draft = False)
    university_to_form = University.objects.all().filter(set_draft = False)
    level_to_form = DiciplineTag.objects.all().filter(set_draft = False)
    
    base_page_continent = None
    base_page_university = None
    base_page_dicipline = None
    try:
        base_page_dicipline = BasePage.objects.get(page_name = 'Diciplines')
        base_page_continent = BasePage.objects.get(page_name = 'Continents')
        base_page_university = BasePage.objects.get(page_name = 'Universities')
    except:
        pass

    dicipline_to_form = dicipline_to_navebar

    form = ApplyForm(request.POST or None)

    context = {
        'base_page_continent':base_page_continent,
        'base_page_university':base_page_university,
        'base_page_dicipline':base_page_dicipline,
        'dicipline_to_navebar' :dicipline_to_navebar,
        'dicipline_to_form' :dicipline_to_form,
        'university_to_form' :university_to_form,
        'country_to_form' :country_to_form,
        'level_to_form' :level_to_form,
        'form':form,
    }
    return render(request, 'contact_form/quick-apply.html', context)

def getDicipline(request):
    if request.is_ajax():
        dicipline = request.POST.get('dicipline')
        level = request.POST.get('level')

        get_specialty = Speciality.objects.all().filter(
            set_draft = False,
            dicipline = dicipline,
            study_level = level,
        )

        return JsonResponse(
            {
                'get_specialty':get_specialty,
            }
        )

def getSpecialty(request):
    if request.is_ajax():
        specialty = request.POST.get('specialty')

        get_program = Speciality.objects.all().filter(
            set_draft = False,
            program_speciality = specialty
        )

        return JsonResponse(
            {
                'program_name':get_specialty.program_name,
            }
        )