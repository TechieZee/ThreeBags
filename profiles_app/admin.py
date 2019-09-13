from django.contrib import admin
from .models import College, Stream, Student
# Register your models here.
admin.site.register(Stream)
admin.site.register(College)
admin.site.register(Student)