from django.urls import URLPattern
from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    
]