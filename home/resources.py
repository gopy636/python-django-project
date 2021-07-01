
from .models import *
from import_export import resources

class StudentResource(resources.ModelResource):

    class Meta:
        model = Student
        
