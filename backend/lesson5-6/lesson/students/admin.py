from django.contrib import admin
from students.models import Student, StudentGroup, Subject
# Register your models here.
admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Subject)