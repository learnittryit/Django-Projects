from django.contrib import admin

# Register your models here.

#Importing models
from .models import Project

#Registering models
""" This line says I want to see this project inside the admin, therefore I am registering this model"""
admin.site.register(Project)
