import threading
from django.conf import settings
from django.core.mail import EmailMessage


class EmailAttchment(threading.Thread):


    def __init__(self, email, name):

        threading.Thread.__init__(self)
        self.email=email
        self.name=name
        



    def run(self):
        try:
            subject = 'please find attachment'
            body = f'Hey there i am  {self.name}  sending you excel format data of student please find attachment' 
            email_from = settings.EMAIL_HOST_USER
            mail=EmailMessage(subject ,body , email_from ,[self.email])
            mail.attach_file("media/output/excel.xlsx")
            print('SEND EMAIL STARTED')
            mail.send()
            print('EMAIL SENT')
        except Exception as e:
                print(e)
