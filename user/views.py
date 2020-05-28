from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def login(request):
    return render (request,'user/login.html')

def homepage(request):
    return render (request,'user/home.html')

def logout_view(request):
    logout(request)
    return redirect('home',permanent = True )

def about(request):
    return render (request,'user/about.html')
