from rest_framework import serializers
from .import models



class ServiceslotSerializer(serializers.ModelSerializer):
    # customer = serializers.SlugRelatedField(queryset=models.User.objects.all(), slug_field='first_name') 
    service = serializers.SlugRelatedField(queryset=models.Service.objects.all(), slug_field='Name') 
    
    class Meta:
        model=models.ServiceSlot
        fields='__all__'
        # exclude=['service_status']


class ordersinfoseralizer(serializers.ModelSerializer):
    class Meta:
        model=models.customerorderinfo
        fields='__all__'