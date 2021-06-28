from django.conf import settings
from django.core.mail import send_mail
import time




def send_activation_email(email , first_name , token):
    try:

        subject = 'Your accounts needs to verified'
        message = f'Hi {first_name}, Otp for activate your account {token}'
        email_from = settings.EMAIL_HOST_USER 
        print('SEND EMAIL STARTED')
        send_mail(subject , message ,email_from ,[email])
        print('EMAIL SENT')


    except Exception as e:
        print(e)
        
