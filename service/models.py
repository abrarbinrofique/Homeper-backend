from typing import Any
from django.db import models
from customer.models import Customer
from cloudinary.models import CloudinaryField

STAR_CHOICE={
   ( 1,'⭐'),
    (2,'⭐⭐'),
    (3,'⭐⭐⭐'),
    (4,'⭐⭐⭐⭐'),
    (5,'⭐⭐⭐⭐⭐')
}

# Create your models here.
class Service(models.Model):
    Name=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    image =CloudinaryField('image')
    description=models.TextField()

    def __str__(self):
        return self.Name




class ReviewModel(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    service=models.ForeignKey(Service, on_delete=models.CASCADE)
    ratting=models.IntegerField(choices=STAR_CHOICE)
    textreview=models.TextField()


   




