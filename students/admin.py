from django.contrib import admin
from .models import Students,Speciality
# Register your models here.
#adding students and speciality to admin view
admin.site.register(Students)
admin.site.register(Speciality)
