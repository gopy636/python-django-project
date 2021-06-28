import threading
from django.conf import settings
from django.core.mail import send_mail
import time
from django.core.cache import cache


class SendOtpEmail(threading.Thread):
    def __init__(self , email , first_name ,otp):
        self.email = email
        self.first_name = first_name
        self.otp = otp
        threading.Thread.__init__(self)
    
    def run(self):
        time.sleep(20)
        try:
            subject = 'Your accounts needs to verified'
            message = f'Hi {self.first_name}, otp for activate your account {self.otp}'
            email_from = settings.EMAIL_HOST_USER 
            print('SEND EMAIL STARTED')
            cache.set(self.otp , self.email, timeout=60*120)
            send_mail(subject , message ,email_from ,[self.email])
            print('EMAIL SENT')
        except Exception as e:
            print(e)
