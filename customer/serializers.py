from rest_framework import serializers
from .models import Customer 
from django.contrib.auth.models import User
class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username') 
    class Meta:
        model=Customer
        fields="__all__"

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)
    dp = serializers.ImageField(required=False, allow_null=True)
    bio = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.CharField(required=False, allow_null=True, max_length=11)
    fb = serializers.CharField(required=False, allow_null=True, max_length=50)
    ln = serializers.CharField(required=False, allow_null=True, max_length=50)
    x = serializers.CharField(required=False, allow_null=True, max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'dp', 'bio', 'phone', 'fb', 'ln', 'x']

    def create(self, validated_data):
        # Extract User fields
        user_data = {
            'username': validated_data['username'],
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
            'email': validated_data['email'],
        }
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({'password': "Passwords don't match."})

        user = User.objects.create(**user_data)
        user.set_password(password)
        user.is_active = False
        user.save()

        # Extract and create Customer
        customer_data = {
            'user': user,
            'dp': validated_data.get('dp', None),
            'bio': validated_data.get('bio', ''),
            'phone': validated_data.get('phone', ''),
            'fb': validated_data.get('fb', ''),
            'ln': validated_data.get('ln', ''),
            'x': validated_data.get('x', '')
        }
        Customer.objects.create(**customer_data)
        
        return user
class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
       