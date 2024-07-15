from django.db import models
from rest_framework import serializers

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    problems=models.TextField()


    def __str__(self):
        return f"{self.name}"
    

    class Meta:
        verbose_name_plural="Contact US"
