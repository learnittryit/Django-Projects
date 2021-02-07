"""
# Kunal has copied from the portfoli's urls.py
"""



from django.urls import path
from . import views # we used "dot" becuase its in the same folder

urlpatterns = [
    path('',views.all_blogs,name='all_blogs'),
]
