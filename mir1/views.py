from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import users
from .forms import SignUP
# Create your views here.


def home_view(request):
	return render(request,"home.html",{})


def registerpage(request):
    if request.method == "POST":
        Data = request.POST
        user = User.objects.create_user(username = Data['username'], password = Data['password1'],email = Data['email'],)
        M = users(user_id = Data['userid'],user_name =Data['username'],user_state = Data['userstatechoices'],phone_number = Data['phonenumber'],email=Data['email'],)
        M.save()
        user_form = SignUP(request.POST)
        if user_form.is_valid():
            user_form.save()
        login(request, user)
        return redirect('home')

    elif request.method == "GET":
        return render(request, 'register.html',{})


def loginpage(request):
    context= {'User' : User}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, "Username Or Password Is Incorrect :(")
            return render (request,'login.html',context)
    
    return render (request,'login.html', context)

def contactspage(request):
    return render(request,"contacts.html")

def logoutuser(request):
    logout(request)
    return redirect('login')