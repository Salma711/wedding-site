from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            messages.error(request, "Invalid")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            
            if not remember_me:
                request.session.set_expiry(0)
            messages.success(request, "You logged in successfuly")
            return redirect('/')
            
        else:
            messages.error(request,'invalid')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def user_logout(request):
    auth.logout(request)
    messages.success(request, "You logged out successfuly")
    return redirect('/')
