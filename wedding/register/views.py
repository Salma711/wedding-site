from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            print("User saved to the database")
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login(request):
    user = None
    remember_me = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('/')
        else:
            messages.error(request,'invalid')
    else:
     form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
def logout(request):
    auth.logout(request)
    return redirect('/')
