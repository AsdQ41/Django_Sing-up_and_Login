from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'sing/sugnup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('http://127.0.0.1:8000/ready/')
            except IntegrityError:
                return render(request, 'sing/sugnup.html', {'form': UserCreationForm(), 'error': 'This name is taken. Please create a new'})
        else:
            return render(request, 'sing/sugnup.html', {'form': UserCreationForm(), 'error': 'Password is did not match'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect("http://127.0.0.1:8000/ready/")




def home(request):
    return render(request, 'sing/index.html', )

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'sing/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'sing/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and Password did not match'})
        else:
            login(request, user)
            return redirect("http://127.0.0.1:8000/ready/")

def ready(request):
    return render(request, 'sing/accept.html')

