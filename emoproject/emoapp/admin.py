from unicodedata import name
from django.contrib import admin
from .models import *
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    search_fields= ['email','name','Mobileno']


admin.site.register(Todo,TodoAdmin)

