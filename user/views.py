from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def login(request):
    return render (request,'user/login.html')
