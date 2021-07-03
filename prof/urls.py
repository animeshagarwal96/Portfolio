from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('resume',views.resume,name="resume"),
    path('business',views.business,name="business"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="login"),
    path('logout',views.handlelogout,name="logout")
]