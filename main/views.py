from django.contrib import messages
from django.db.models.fields import related
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.http import JsonResponse
from .forms import *
from django.urls import reverse
from post.models import BlogPost

import datetime
# Create your views here.
def index(request):
    # To display items in nav bar
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)
    
    base_page_dicipline = BasePage.objects.get(page_name = 'Diciplines')
    

    # Display featured program on the home page
    feature_dicipline = Dicipline.objects.all().filter(set_featured = True, set_draft = False).order_by('short_name')[:14]

    feature_dicipline_count = feature_dicipline.count()

    # display countries on the home page
    featured_coutries = Country.objects.all().filter(set_draft = False).order_by('-date_created')[:6]
    
    # featured universities on  the home page
    featured_universities = University.objects.all().filter(set_draft = False).order_by('-date_created')[:8]

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]
    context = {
        'base_page_dicipline':base_page_dicipline,
        'feature_dicipline_count':feature_dicipline_count,
        'featured_universities':featured_universities,
        'featured_coutries':featured_coutries,
        'featured_post':featured_post,
        'dicipline_to_navebar':dicipline_to_navebar,
        'feature_dicipline':feature_dicipline,
    }
    return render(request, 'main/main-home-page.html', context)


def articlePage(request, article):
    # To display items in nav bar and Category page
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False)
    
    # Page content
    get_article = BasePage.objects.get(page_name = article, set_draft = False)
    dicipline = get_article.dicipline_set.all().filter(set_draft = False).order_by('short_name')
    university = get_article.university_set.all().filter(set_draft = False).order_by('-date_created')
    speciality = get_article.speciality_set.all().filter(set_draft = False).order_by('-date_created')
    country = get_article.country_set.all().filter(set_draft = False).order_by('-date_created')


    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

    context = {
        'country':country,
        'speciality':speciality,
        'university':university,
        'dicipline':dicipline,
        'featured_post':featured_post,
        'dicipline_to_navebar':dicipline_to_navebar,
    }

    if get_article.page_name == 'Diciplines':
        return render(request, 'main/dicipline-page.html', context)
    elif get_article.page_name == 'Universities':
        return render(request, 'main/university-page.html', context)
    elif get_article.page_name == 'Specialties':
        return render(request, 'main/speciality-page.html', context)

    elif get_article.page_name == 'Continents':
        return render(request, 'main/countries-page.html', context)
        

def singleDicipline(request, dicipline_url):
    # To display items in nav bar
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)

    # GEt Dicipline
    single_dicipline = Dicipline.objects.get(short_name =dicipline_url, set_draft = False)

    master_level = DiciplineTag.objects.get(name = 'Master')
    bachelor_level = DiciplineTag.objects.get(name = 'Bachelor')
    phd_level = DiciplineTag.objects.get(name = 'PhD')

    speciality_in_dicipline = single_dicipline.speciality_set.all().filter(set_draft = False)
    speciality_in_dicipline_count = speciality_in_dicipline.count()

    master_speciality = speciality_in_dicipline.filter(study_level = master_level)
    bachelor_speciality = speciality_in_dicipline.filter(study_level = bachelor_level)
    phd_speciality = speciality_in_dicipline.filter(study_level = phd_level)

    # program_in_dicipline = single_dicipline.program_set.all().filter(set_draft = False)
    # program_in_dicipline_count = program_in_dicipline.count()

    context = {
        'phd_speciality':phd_speciality,
        'bachelor_speciality':bachelor_speciality,
        'master_speciality':master_speciality,
        # 'program_in_dicipline_count':program_in_dicipline_count,
        'speciality_in_dicipline_count':speciality_in_dicipline_count,
        'speciality_in_dicipline':speciality_in_dicipline,
        'single_dicipline':single_dicipline,
        'dicipline_to_navebar':dicipline_to_navebar,
    }
    return render(request, 'main/single-dicipline.html', context)


def singleSpeciality(request, speciality_url):
    # To display items in nav bar
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)

    spaciality = Speciality.objects.get(speciality_name = speciality_url, set_draft = False)

    related_university = spaciality.university_set.all().filter(set_draft = False).order_by('-date_created')
    related_university_count = related_university.count()

    related_program = spaciality.program_set.all().filter(set_draft = False)

    
    
    context = {
        'related_program':related_program,
        'related_university_count':related_university_count,
        'related_university':related_university,
        'spaciality':spaciality,
        'dicipline_to_navebar':dicipline_to_navebar,
    }
    return render(request, 'main/signle-speciality.html', context)


def singleUniversity(request, university_url):
    # To display items in nav bar
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)

    university = University.objects.get(university_name = university_url)

    university_fact = university.universityfact_set.all().filter(set_draft = False).order_by('-date_created')

    program = university.program_set.all().filter(set_draft = False).order_by('-date_created')

    master_level = DiciplineTag.objects.get(name = 'Master')
    bachelor_level = DiciplineTag.objects.get(name = 'Bachelor')
    phd_level = DiciplineTag.objects.get(name = 'PhD')

    master_speciality = program.filter(study_level = master_level)
    bachelor_speciality = program.filter(study_level = bachelor_level)
    phd_speciality = program.filter(study_level = phd_level)

    context = {
        'phd_speciality':phd_speciality,
        'bachelor_speciality':bachelor_speciality,
        'master_speciality':master_speciality,
        'program':program,
        'university_fact':university_fact,
        'university':university,
        'dicipline_to_navebar':dicipline_to_navebar,
    }
    return render(request, 'main/single-university.html', context)


# def programPage(request):
#     # To display items in nav bar
#     category_to_navebar = Speciality.objects.all().filter(set_draft = False, set_featured = True)

#     # Query programs for the select form field
#     program_to_form = Program.objects.all().filter(set_draft = False)

#     # Query all programs
#     all_programs = Program.objects.all().filter(set_draft = False)

#     # Featured post on page bottum
#     featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

#     context = {
#         'program_to_form':program_to_form,
#         'featured_post':featured_post,
#         'all_programs':all_programs,
#         'category_to_navebar':category_to_navebar,
#     }

#     return render(request, 'main/program.html', context)

# def singleProgram(request, program_url):
#     # To display items in nav bar
#     category_to_navebar = Speciality.objects.all().filter(set_draft = False, set_featured = True)

#     # Query programs for the select form field
#     program_to_form = Program.objects.all().filter(set_draft = False)

#     # Query sigle programe
#     single_program = Program.objects.get(program_name = program_url, set_draft = False)
#     program_fact = single_program.programfact_set.all().filter(set_draft = False)

#     # Featured post on page bottum
#     featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

#     context = {
#         'program_to_form':program_to_form,
#         'featured_post':featured_post,
#         'program_fact':program_fact,
#         'single_program':single_program,
#         'category_to_navebar':category_to_navebar,
#     }

#     return render(request, 'main/single-program.html', context)


def singleCountry(request, country_url):
    # To display items in nav bar
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)

    single_country = Country.objects.get(country_name=country_url, set_draft = False)

    related_universities = single_country.university_set.all().filter(set_draft = False)
    country_fact = single_country.countryfact_set.all().filter(set_draft = False).order_by('-date_created')

    context = {
        'country_fact':country_fact,
        'related_universities':related_universities,
        'single_country':single_country,
        'dicipline_to_navebar':dicipline_to_navebar,
    }
    return render(request, 'main/single-country.html', context)



def contactUsPage(request):
    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]
    # To display items in nav bar
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)

    form = ContactForm(request.POST)

    if request.is_ajax():
        if form.is_valid():
            form.save()

            return JsonResponse({
                'message': 'Your request has been submited, w\'ll get back to you as soon as possible'
            })
        else:
            return JsonResponse({
                'error': 'Error !, your form can not be submited'
            })

    context = {
        'form':form,
        'featured_post':featured_post,
        'dicipline_to_navebar':dicipline_to_navebar,
    }
    return render(request, 'main/contact-page.html', context)


def aboutUsPage(request):
    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]
    # To display items in nav bar
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)

    context = {
        'featured_post':featured_post,
        'dicipline_to_navebar':dicipline_to_navebar,
    }
    return render(request, 'main/about-us.html', context)

def successPage(request):
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)

    context = {
        'dicipline_to_navebar':dicipline_to_navebar,
    }
    return render(request, 'success-page.html', context)

# Custun error handler page
def error_404(request, exception):
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)

    context = {
        'dicipline_to_navebar':dicipline_to_navebar,
    }
    return render(request, 'main/404.html', context)

def error_400(request, exception):
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)

    context = {
        'dicipline_to_navebar':dicipline_to_navebar,
    }
    return render(request, 'main/404.html', context)

def error_500(request):
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)

    context = {
        'dicipline_to_navebar':dicipline_to_navebar,
    }
    return render(request, 'main/404.html', context)

def error_403(request, exception):
    dicipline_to_navebar = Dicipline.objects.all().filter(set_draft = False, set_featured = True)

    context = {
        'dicipline_to_navebar':dicipline_to_navebar,
    }
    return render(request, 'main/404.html', context)
