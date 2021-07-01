from os import name
from django.db import models

# Create your models here.


class HandleExcel(models.Model):
    excel_file=models.FileField(upload_to='excel')

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=3)
    email=models.EmailField(max_length=100)
    adress=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Email(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    