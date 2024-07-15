from django.shortcuts import render
from .import models
from .import serializers
from rest_framework import viewsets
# Create your views here.



class ServiceslotViewset(viewsets.ModelViewSet):
    queryset=models.ServiceSlot.objects.all()
    serializer_class=serializers.ServiceslotSerializer


    def get_queryset(self):
        queryset=super().get_queryset()
        customer_id=self.request.query_params.get('customer_id')
        if customer_id:
            queryset=queryset.filter(customer_id=customer_id)
           

        return queryset