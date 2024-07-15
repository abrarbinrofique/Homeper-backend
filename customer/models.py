from django.db import models

# Create your models he
from django.contrib.auth.models import User


class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    dp=models.ImageField(upload_to='customer/media/')
    bio=models.TextField()
    phone=models.CharField(max_length=11)
    fb=models.CharField(blank=True,null=True,max_length=50)
    ln=models.CharField(blank=True,null=True,max_length=50)
    x=models.CharField(blank=True,null=True,max_length=50)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} "