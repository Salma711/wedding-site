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
            form.save()
        return redirect("/") 
    else:
        form = RegisterForm()
    return render(request, "base.html", {"form": form})

def login(request):
    user = None
    remember_me = None
    if request.method == 'POST':
        form2 = LoginForm(request.POST)
        if form2.is_valid():
            email = form2.cleaned_data['email']
            password = form2.cleaned_data['password']
            remember_me = form2.cleaned_data.get('remember_me')['']
            user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        if not remember_me:
            request.session.set_expiry(0)
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('/')
    else:
     form2 = LoginForm()
    return render(request, 'base.html', {'form2': form2})
def logout(request):
    auth.logout(request)
    return redirect('/')
