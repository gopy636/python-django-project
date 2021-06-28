from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import messages
from .utils import *
import random
from .thread import *

# token -> 24hr  - [ active ] ! [error invalid token token expired]

def register(request):

    if request.method == 'POST':
        email   = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        otp = random.randint(10000,99998)
        
        user_obj = User(
            email = email, 
            phone_number = phone_number,
            otp = otp
        )
        user_obj.set_password(password)
        user_obj.save()

        
        SendOtpEmail(email,"gopal",otp).start()

        messages.info(request, 'Account created.')
        return render(request, 'verify.html')
    return render(request, 'register.html')



def verify_user(request ,otp):
    try:
        if not cache.get(otp):
            return HttpResponse('Your otp has expired or invalid')
        
        print(cache.ttl(otp)) 

        user_obj = User.objects.get(otp =otp)
        user_obj.is_verified = True
        user_obj.save()
        return HttpResponse('Your account is verified')
        return render(request, 'login.html')
    except Exception as e:
        print(e)
    return HttpResponse('Invalid Token')

def get_otp(request):
    if request.method=="POST":
        otp =request.POST.get("Otp")
        return redirect("verify-account",otp)
        
def login_attempt(request):
    if request.method == 'POST':
        email   = request.POST.get('email')
        password = request.POST.get('password')
        return redirect('/verify/')
 
    return render(request , 'login.html')
