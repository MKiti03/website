from django.views.generic import ListView
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

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]
    context = {
        'featured_post':featured_post,
        'category_to_navebar':category_to_navebar,
        'feature_program':feature_program,
    }
    return render(request, 'main/main-home-page.html', context)

def programCategory(request):
    # To display items in nav bar and Category page
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

    context = {
        'featured_post':featured_post,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/category-page.html', context)

def singleProgramCategory(request, category_url):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    # GEt fategorie programs
    program_category = ProgramCategory.objects.get(program_category_title =category_url, set_draft =False)

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

    program = program_category.program_set.all().filter(set_draft = False)

    context = {
        'featured_post':featured_post,
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

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

    context = {
        'featured_post':featured_post,
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

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

    context = {
        'featured_post':featured_post,
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

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]


    context = {
        'featured_post':featured_post,
        'all_countries':all_countries,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/countries.html', context)

def singleCountry(request, country_url):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    single_country = Country.objects.get(country_name=country_url, set_draft = False)

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

    country_fact = single_country.countryfact_set.all().filter(set_draft = False)
    related_universities = single_country.university_set.all().filter(set_draft = False)
    universities_count = related_universities.count()

    print(related_universities)

    context = {
        'featured_post':featured_post,
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

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

    context = {
        'featured_post':featured_post,
        'all_universities':all_universities,
        'category_to_navebar':category_to_navebar,
    }

    return render(request, 'main/university.html', context)

def singleUniversity(request, university_url):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

    single_university = University.objects.get(university_name=university_url, set_draft = False)

    university_fact = single_university.universityfact_set.all().filter(set_draft = False)

    university_program = single_university.program_set.all().filter(set_draft = False)
    university_program_count = university_program.count()

    context = {
        'featured_post':featured_post,
        'university_program_count':university_program_count,
        'university_program':university_program,
        'university_fact':university_fact,
        'single_university':single_university,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/single-university.html', context)


def postCategory(request):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

    post_category = PostCategory.objects.all().filter(set_draft = False)


    context = {
        'featured_post':featured_post,
        'post_category':post_category,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/post-category.html', context)

def singlePostCategory(request, post_category_url):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

    single_post_category = PostCategory.objects.get(post_category_title = post_category_url, set_draft = False)
    post_content = single_post_category.blogpost_set.all().filter(set_draft = False)
    context = {
        'featured_post':featured_post,
        'post_content':post_content,
        'single_post_category':single_post_category,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/single-post-category.html', context)

class BlogPostPage(ListView):
    queryset = BlogPost.objects.filter(set_draft = False).order_by('-date_created')

    #Display programs category on the navbar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]
    
    template_name = 'main/blog-post.html'

    paginate_by = 16
    
    extra_context = {
        'featured_post':featured_post,
        'category_to_navebar':category_to_navebar,
    }

def singlePost(request, single_post_url):
    # To display items in nav bar
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)

    single_post = BlogPost.objects.get(post_title = single_post_url, set_draft = False)
    post_tag = single_post.tag_set.all().filter(set_draft = False)

    post_comment = single_post.postcomment_set.all().filter(set_draft = False).order_by('-date_created')
    post_comment_count = post_comment.count()
    context = {
        'post_comment_count':post_comment_count,
        'post_comment':post_comment,
        'post_tag':post_tag,
        'single_post':single_post,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/blog-post-single.html', context)

def error_404(request, exception):
    return render(request, 'main/404.html')