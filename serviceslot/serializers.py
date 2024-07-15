from rest_framework import serializers
from .import models



class ServiceslotSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(queryset=models.Customer.objects.all(), slug_field='user.first_name') 
    service = serializers.SlugRelatedField(queryset=models.Service.objects.all(), slug_field='Name') 
    
    class Meta:
        model=models.ServiceSlot
        exclude=['created_time','service_status']