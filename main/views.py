from main.forms import UserProfileForm
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def index(request):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)
    # Display featured program on the home page
    feature_program = Program.objects.all().filter(set_featured = True, set_draft = False)
    context = {
        'category_to_navebar':category_to_navebar,
        'feature_program':feature_program,
    }
    return render(request, 'main/main-home-page.html', context)

def programCategory(request):
    # To display items in nav bar and Category page
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)
    # Program pers category count

    context = {
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/category-page.html', context)

def singleProgramCategory(request, category_url):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    # GEt fategorie programs
    program_category = ProgramCategory.objects.get(program_category_title =category_url, set_draft =False)

    program = program_category.program_set.all().filter(set_draft = False)

    context = {
        'program_category':program_category,
        'program':program,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/single-category.html', context)

def programPage(request):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    # Query all programs
    all_programs = Program.objects.all().filter(set_draft = False)

    context = {
        'all_programs':all_programs,
        'category_to_navebar':category_to_navebar,
    }

    return render(request, 'main/program.html', context)

def singleProgram(request, program_url):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    # Query sigle programe
    single_program = Program.objects.get(program_name = program_url, set_draft = False)
    program_fact = single_program.programfact_set.all().filter(set_draft = False)

    context = {
        'program_fact':program_fact,
        'single_program':single_program,
        'category_to_navebar':category_to_navebar,
    }

    return render(request, 'main/single-program.html', context)


def countryPage(request):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)
    # Query all countries
    all_countries = Country.objects.all().filter(set_draft = False)


    context = {
        'all_countries':all_countries,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/countries.html', context)

def singleCountry(request, country_url):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    single_country = Country.objects.get(country_name=country_url, set_draft = False)

    country_fact = single_country.countryfact_set.all().filter(set_draft = False)
    related_universities = single_country.university_set.all().filter(set_draft = False)
    universities_count = related_universities.count()

    print(related_universities)

    context = {
        'related_universities':related_universities,
        'universities_count':universities_count,
        'country_fact':country_fact,
        'single_country':single_country,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/single-country.html', context)



def universityPage(request):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    all_universities = University.objects.all().filter(set_draft = False)

    context = {
        'all_universities':all_universities,
        'category_to_navebar':category_to_navebar,
    }

    return render(request, 'main/university.html', context)

def singleUniversity(request, university_url):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    single_university = University.objects.get(university_name=university_url, set_draft = False)

    university_fact = single_university.universityfact_set.all().filter(set_draft = False)

    university_program = single_university.program_set.all().filter(set_draft = False)
    university_program_count = university_program.count()

    context = {
        'university_program_count':university_program_count,
        'university_program':university_program,
        'university_fact':university_fact,
        'single_university':single_university,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/single-university.html', context)


def blogPostPage(request):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)


    context = {
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/blog-post.html', context)

def singlePost(request):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)


    context = {
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/blog-post-single.html', context)
