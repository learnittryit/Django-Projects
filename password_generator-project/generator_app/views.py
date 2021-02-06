from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    print("------------------------->",request.get_full_path())
    if(request.get_full_path()=='/kunal-path/'):
        return HttpResponse('<h1>hello there friend Kunal we did it !!</h1>');
    else:
        return HttpResponse('Hi dude!!!  You did not request anything')

def eggs(request):
    return HttpResponse('<h2>kunal love eggs</h2>')

def callTemplate(request):
        return render(request,'generator_app_templates/kunalHome.html',{'password':'random-pwd'})

def homePage(request):
    return render(request,'generator_app_templates/homePage.html',{'pwd':'randon-password-encryted'})

def password(request):
    return render(request,'generator_app_templates/password.html')

"""
Generating -password -start
"""
def generate_password(request):

    thePassword='pwd-testing'
    characters = list('abcdefghijklmnopqrstuvwxyz')

    # Extending List with upper case
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # Extending list with special Characters
    if request.GET.get('specialChar'):
        characters.extend(list('~!@#$%^&*()_-'))

    # Extending list with Numbers
    if request.GET.get('numbers'):
        characters.extend([str(i) for i in range(10)])

    # length
    default_length=10
    length = int(request.GET.get('length',default_length))


    for i in range(length):
        thePassword+=random.choice(characters)

    return render(request,'generator_app_templates/g_password.html',{'password':thePassword})

def homePage_1(request):
    return render(request,'generator_app_templates/homePage_1.html',{'pwd':'home_1_new_random_password'})
