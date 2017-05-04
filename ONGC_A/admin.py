from django.contrib import admin

# Register your models here.

from .models import Student, Week, Lecture

admin.site.register(Student)
admin.site.register(Week)
admin.site.register(Lecture)