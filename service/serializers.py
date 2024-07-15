from rest_framework import serializers
from .models import Service,ReviewModel
from django.db.models import Avg
from .import models
from django.contrib.auth.models import User

class ServiceSerializers(serializers.ModelSerializer):
     average_rating = serializers.SerializerMethodField()

   

     class Meta:
          model=Service
          fields='__all__'



     def get_average_rating(self, obj):
       
        average_rating = ReviewModel.objects.filter(service=obj).aggregate(Avg('ratting'))['ratting__avg']
        return round(average_rating, 2) if average_rating else None









    

class ReviewSerializer(serializers.ModelSerializer):
#     customer = serializers.SlugRelatedField(queryset=models.Customer.objects.all(), slug_field='user.first_name') 
    service = serializers.SlugRelatedField(queryset=models.Service.objects.all(), slug_field='Name') 
    class Meta:
          model=ReviewModel
          fields='__all__'


