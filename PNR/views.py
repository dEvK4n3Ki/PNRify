#django Imports
import time
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.template.response import TemplateResponse

#Selenium Imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

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

def goair_verify(request):
    if request.method == 'POST':
        pnr = request.POST.get('pnr')
        lname = request.POST.get('lname')
        book_date = request.POST.get('book_date')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver_goair = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=chrome_options)
        driver_goair.get('https://www.goair.in/plan-my-trip/manage-booking')
        driver_goair.implicitly_wait(10)
        driver_goair.find_element(By.NAME, "PNR").send_keys(pnr)
        driver_goair.find_element(By.NAME,"FirstName").send_keys(lname)
        driver_goair.find_element_by_xpath('//button[normalize-space()="Retrieve Booking"]').click()
        try:
            myElem = WebDriverWait(driver_goair, 5).until(EC.title_is("GoAir | Airline Tickets and Fares - Itinerary"))
            URL_current = driver_goair.current_url
            redirect_url = "https://book.goair.in/Booking"
            if URL_current == redirect_url:
                return render(request,'PNR/GoAir.html',{'check':True ,'auth_status':True})
            else:
                return render(request,'PNR/GoAir.html',{'check':True , 'auth_status':False})

        except TimeoutException:
            return render(request,'PNR/GoAir.html',{'check':True , 'auth_status':False})


def indigo_landing(request):
    return render(request, 'PNR/Indigo.html', {"check":False})

def indigo_verify(request):
    if request.method == 'POST':
        pnr = request.POST.get('pnr')
        lname = request.POST.get('lname')
        book_date = request.POST.get('book_date')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=chrome_options)
        driver.get('https://www.goindigo.in/member/my-booking.html')
        driver.implicitly_wait(10)
        driver.find_element(By.NAME, "booking").send_keys(pnr)
        driver.find_element(By.NAME,"email").send_keys(lname + Keys.RETURN)
        try:
            myElem = WebDriverWait(driver, 5).until(EC.title_is("Itinerary"))
            URL_current = driver.current_url
            redirect_url = "https://www.goindigo.in/booking/view.html"
            if URL_current == redirect_url:
                return render(request,'PNR/Indigo.html',{'check':True ,'auth_status':True})
            else:
                return render(request,'PNR/Indigo.html',{'check':True , 'auth_status':False})

        except TimeoutException:
            return render(request,'PNR/Indigo.html',{'check':True , 'auth_status':False})
