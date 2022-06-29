from ast import Num
import email
from email.headerregistry import Address
from email.policy import default
from django.db import models
# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    Mobileno = models.BigIntegerField(max_length=10)
    Address = models.CharField(max_length=500)
    email = models.EmailField(max_length=200,default=True)
    search_fields = ['email','name','Mobileno']
    def __str__(self):
        return self.name
    
    
    



