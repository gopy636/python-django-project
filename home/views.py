from django.shortcuts import render

# Create your views here.
from django .http import HttpResponse
from django.shortcuts import redirect, render
import pandas as pd
from .models import *
from .thread import *
def excel_import(request):
     if request.method == "POST":
         excel_file = request.FILES['excel_file']
            
         handle_file = HandleExcel.objects.create(excel_file = excel_file)
         print(handle_file)

         stud_objs=list(Student.objects.all())
         df=pd.DataFrame(stud_objs)
         datas = df.to_excel('media/output/excel.xlsx')
         print(datas)
         return redirect('/home/excel-upload/')
     return render(request , 'excel-import.html')

from django.http import HttpResponse
from .admin import StudentResource
from django.core.files.base import ContentFile

def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        stu_resource = StudentResource()
        dataset = stu_resource.export()
        
        
        if file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   

    return render(request, 'excel.html')


def send_attachment(request):

    if request.method == 'POST':
        email   = request.POST.get('email')
        name = request.POST.get('name')
        user_obj = Email(
            email = email, 
            name = name,
        )
        user_obj.save()
        print(email)
        thread_obj = EmailAttchment(email,'Gopal')
        thread_obj.start()
        return  HttpResponse('mail send please check your mail box')
    return render(request, 'sendmail.html')

def sendemail_toall(request):
    user_objs=Email.objects.all()
    for user_obj in user_objs:
        thread_obj = EmailAttchment(user_obj.email,'Gopal')
        thread_obj.start()
        return  HttpResponse('mail send please check your mail box')
    return render(request, 'sendall.html')
