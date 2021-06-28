
from django.contrib import admin
from django.urls import path
from account .views import *

urlpatterns = [
    path('register/', register),
    path('get/', get_otp,name="get_otp"),
    path('verify/<otp>/',verify_user, name='verify-account'),
]
