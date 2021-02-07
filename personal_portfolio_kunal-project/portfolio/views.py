from django.shortcuts import render
from .models import Project # Where Project is the name of our class

# Create your views here.
def homePage(request):
    projects=Project.objects.all();#Objects method will get all the objects
    return render(request,'mytemplates/homePage.html',{'projectsVariable':projects}) #Kunal Learning is / produced an error
