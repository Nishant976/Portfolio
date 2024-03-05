from django.db import models

# Create your models here.

class form(models.Model):
    name = models.CharField(max_length=500,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    subject=models.CharField(max_length=50)
    describe=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

