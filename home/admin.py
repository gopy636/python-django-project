from django.contrib import admin
from import_export import resources

from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin

from .models import *
from.resources import StudentResource

class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource


class StudentAdmin(ExportActionMixin, admin.ModelAdmin):
    class Meta:
        model = Student
        
admin.site.register(Student,StudentAdmin)
admin.site.register(HandleExcel)
admin.site.register(Email)


