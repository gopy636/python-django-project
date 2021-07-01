from django.contrib import admin
from django.urls import path
from.views import *

urlpatterns = [
    path('simple-upload/' ,export_data),
    path('excel-upload/' ,excel_import),
    path('send-email', send_attachment),
    path('send-all',sendemail_toall)
]


 