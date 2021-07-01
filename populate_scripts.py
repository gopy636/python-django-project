import os ,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Excelproject.settings")
django.setup()


from home.models import Student
from  django.utils import timezone
from faker import Faker
fake=Faker()

def populate(n):
    for _ in range(n):
            fakename=fake.name()
            fakeemail=fake.email()
            fakeadress= fake.address()
            stud=Student.objects.get_or_create(name=fakename, email=fakeemail, adress=fakeadress)            
populate(20000)
print('data is populate succes')