from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from selenium import webdriver
from django.utils.datastructures import MultiValueDictKeyError

def login_auth(request):
    try:
        if request.method == 'POST':
            uname = request.POST.get('uname')
            pwrd =  request.POST.get('pass')
            user= authenticate(username = uname ,password = pwrd)
            if user is not None:
                request.session['usernm']=uname
                return redirect('dashboard',permanent = True )
            else:
                return render(request, 'user/login.html', {})
            return render(request, 'user/login.html', {})
    except MultiValueDictKeyError:
        return render(request, 'user/login.html', {})

def redirect_to_dash(request):
    uname = request.session.get('usernm')
    if(uname) : del(request.session['usernm'])
    return render(request,'PNR/index.html',{'uname':uname})

def goair_landing(request):
    return render(request, 'PNR/GoAir.html')

def indigo_landing(request):
        return render(request, 'PNR/Indigo.html')

def indigo_verify(request):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.get('http://codepad.org')
    text_area = driver.find_element_by_id('textarea')
    text_area.send_keys("This text is send using Python code.")
    return redirect()
    # driver.get('https://www.goindigo.in/edit-booking.html?linkNav=edit-booking_header')
