from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics

# Create your views here.
class ServiceViewsets(viewsets.ModelViewSet):
    queryset=models.Service.objects.all()
    serializer_class=serializers.ServiceSerializers
  
 
   

    def get_queryset(self):
        
        queryset = models.Service.objects.annotate(avg_ratting=Avg('reviewmodel__ratting')).order_by('-avg_ratting')
        
        return queryset
    




   

class ReviewViewsets(viewsets.ModelViewSet):
    queryset=models.ReviewModel.objects.all()
    serializer_class=serializers.ReviewSerializer


    def get_queryset(self):
        queryset= super().get_queryset()
        service_id=self.request.query_params.get('service_id')
        customer_id=self.request.query_params.get('customer_id')
        if service_id:
            queryset=queryset.filter(service_id=service_id)
        
        if  customer_id:
            queryset=queryset.filter(customer_id=customer_id)
        return queryset





