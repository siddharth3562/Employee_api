from django.db import models

# Create your models here.

class employee(models.Model):
    empid=models.CharField(max_length=10)
    name=models.CharField(max_length=30)
    address=models.TextField()
    position=models.TextField()
    salary=models.IntegerField()
    experiance=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField()
    
