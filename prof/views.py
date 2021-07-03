from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Users,Contact
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'portfolio/home.html')

def business(request):
    return render(request,'portfolio/business.html')

def resume(request):
    return render(request,'portfolio/resume.html')

def contact(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            username = request.user.username
        else:
            username = "No User"
        firstname = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['msg']
        print(firstname)
        print(email)
        print(phone)
        print(message)
        try:
            contact = Contact(username=username,firstname=firstname,email=email,phone=phone,message=message)
            contact.save()
            messages.success(request,"Your Query has been registered succesfully")
            return redirect('home')
        except Exception as e:
            messages.error(request,"Server error occured try again after some time")
            return redirect(request.META.get('HTTP_REFERER'))
    return render(request,'portfolio/contact.html')

def about(request):
    return render(request,'portfolio/about.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['email1']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email1']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if(password != confirm_password):
            messages.error(request,"Password and Confirm Password must match")
        elif(len(password) < 8):
            messages.error(request,"Password length must be 8 or more")
        else:
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
                myUser = Users(username=username,firstname=firstname,lastname=lastname,email=email,password=password)
                myUser.save()
                messages.success(request,"Acount has been successfully created")
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                print(e)
                messages.error(request,"Some thing wrong happen here try again after some time, Thank you")
    return redirect(request.META.get('HTTP_REFERER'))

def handlelogin(request):
    if request.method == "POST":
        username = request.POST['Loginemail']
        password = request.POST['Loginpassword']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been succesfully logged in")
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse('404 - not found')

def handlelogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Successfully logged out')
        return redirect('home')
    else:
        return HttpResponse('404 error')

