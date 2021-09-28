from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from main.models import ProgramCategory


# Create your views here.
def getInTouch(request):

    # To display items in nav bar and Category page
    category_to_navebar = ProgramCategory.objects.all().filter(set_draft = False, set_featured = True)


    context = {
        'category_to_navebar' :category_to_navebar,
    }
    return render(request, 'contact_form/main-page.html', context)