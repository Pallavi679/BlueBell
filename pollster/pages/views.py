from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpRequest 
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from pages.models import Contact
from django.contrib import messages
from datetime import datetime

def index(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    # messages.success(request, 'pallavi
    return render(request, 'home/index.html')
def poll(request):
  return render(request, 'pages/index.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        contact=Contact(name=name,email=email,msg=msg, date=datetime.today())
        contact.save()
        messages.success(request, 'We will connect you! Thank you for connacting us!.')
    return render(request, 'home/contact.html')

def logoutUser(request):
    logout(request)
    return redirect('/signin')

def signup(request):
    if request.method=='POST':
        name=request.POST.get('username')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
       
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if not name.isalnum():
            messages.warning(request, 'Usernameshould contain')
            return redirect('/signup')
        if len(name)>10:
            messages.warning(request, 'Username must be under 10 charcter')
            return redirect('/signup')
        if password!=confirmpassword:
            messages.warning(request, 'Password do not match')
            return redirect('/signup')
        
        user = User.objects.create_user(username=name,email=email,password=password)
        user.first_name=firstname
        user.last_name=lastname
        user.save()
        messages.success(request, "Welcome to Bluebell Online Survey!")
        return redirect('/')

       
    return render(request, 'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome to Bluebell Online Survey!")
            return redirect("/")
        else:
            return render(request, 'sigin.html')
        
    return render(request, 'signin.html')

def about(request):
    return render(request, 'about.html')