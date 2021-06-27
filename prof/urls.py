from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('resume',views.resume,name="resume"),
    path('business',views.business,name="business"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
]