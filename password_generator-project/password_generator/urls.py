"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from generator_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kunal-admin/', admin.site.urls),
    path('kunal-path/',views.home),

    path('',views.homePage_1,name='homePage_1'),# Now this is appeared first so its shown first

    path('',views.homePage),# Same as below- but Kunal first declared is picked up, unlike HashMap

    path('kunal-eggs/',views.eggs),
    path('kunal-home',views.callTemplate),
    path('password/',views.password),
    path('generate-password/',views.generate_password,name='password'),
]
