from django.shortcuts import render
from django.views.generic.list import ListView
from main.models import *
from .models import *

# Create your views here.
def postCategory(request):
    # To display items in nav bar
    category_to_navebar = Speciality.objects.all().filter(set_draft = False, set_featured = True)

    # Query programs for the select form field
    program_to_form = Program.objects.all().filter(set_draft = False)

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

    post_category = PostCategory.objects.all().filter(set_draft = False)


    context = {
        'program_to_form':program_to_form,
        'featured_post':featured_post,
        'post_category':post_category,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/post-category.html', context)

def singlePostCategory(request, post_category_url):
    # To display items in nav bar
    category_to_navebar = Speciality.objects.all().filter(set_draft = False, set_featured = True)
    # Query programs for the select form field
    program_to_form = Program.objects.all().filter(set_draft = False)
    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]

    single_post_category = PostCategory.objects.get(post_category_title = post_category_url, set_draft = False)
    post_content = single_post_category.blogpost_set.all().filter(set_draft = False)
    context = {
        'program_to_form':program_to_form,
        'featured_post':featured_post,
        'post_content':post_content,
        'single_post_category':single_post_category,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/single-post-category.html', context)

class BlogPostPage(ListView):
    queryset = BlogPost.objects.filter(set_draft = False).order_by('-date_created')

    # Query programs for the select form field
    program_to_form = Program.objects.all().filter(set_draft = False)

    #Display programs category on the navbar
    category_to_navebar = Speciality.objects.all().filter(set_draft = False, set_featured = True)

    # Featured post on page bottum
    featured_post = BlogPost.objects.all().filter(set_draft = False, set_featured = True).order_by('-date_created')[:8]
    
    template_name = 'main/blog-post.html'

    paginate_by = 16
    
    extra_context = {
        'program_to_form':program_to_form,
        'featured_post':featured_post,
        'category_to_navebar':category_to_navebar,
    }

def singlePost(request, single_post_url):
    # To display items in nav bar
    category_to_navebar = Speciality.objects.all().filter(set_draft = False, set_featured = True)

    # Query programs for the select form field
    program_to_form = Program.objects.all().filter(set_draft = False)
    single_post = BlogPost.objects.get(post_title = single_post_url, set_draft = False)
    post_tag = single_post.tag_set.all().filter(set_draft = False)

    post_comment = single_post.postcomment_set.all().filter(set_draft = False).order_by('-date_created')
    post_comment_count = post_comment.count()
    context = {
        'program_to_form':program_to_form,
        'post_comment_count':post_comment_count,
        'post_comment':post_comment,
        'post_tag':post_tag,
        'single_post':single_post,
        'category_to_navebar':category_to_navebar,
    }
    return render(request, 'main/blog-post-single.html', context)