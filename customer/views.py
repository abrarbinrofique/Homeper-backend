from django.shortcuts import render
from .import serializers
from .import models
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
#for email sending
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,logout
from django.http import JsonResponse
# Create your views here.
class CustomerViewsets(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        user = User.objects.get(id=user_id)
        serializer.save(user=user)

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class UserRegistraitionView(APIView):
      serializer_class=serializers.RegistrationSerializer


      def post(self,request):
            serializer=self.serializer_class(data=request.data)

            if serializer.is_valid():
                  user=serializer.save()
                  token=default_token_generator.make_token(user)
                  print(token)
                  uid=urlsafe_base64_encode(force_bytes(user.pk))
                  print(uid)
                  confirm_link=f"http://127.0.0.1:8000/customer/active/{uid}/{token}"
                  email_subject="Confirm Your Email"
                  email_body=render_to_string('confirm_email.html',{"confirm_link":confirm_link})
                  email=EmailMultiAlternatives(email_subject," ",to=[user.email])
                  email.attach_alternative(email_body,"text/html")
                  email.send()
                  return Response("check your email for confirmation")
            
            
            return Response(serializer.errors)
      


def activate(request,uid64,token):
            try:
                  uid=urlsafe_base64_decode(uid64).decode()
                  user=User._default_manager.get(pk=uid)
            except(User.DoesNotExist):
                  user=None

            if user is not None and default_token_generator.check_token(user,token):
                  user.is_active=True
                  user.save()
                  return redirect('login')
            else:
                  return redirect('register')


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                customer =models.Customer.objects.get(user=user)
                customer_serializer = serializers.CustomerSerializer(customer)
                return Response({
                    'token': token.key,
                    'user_id': user.id,
                    'customer': customer_serializer.data
                })
            else:
                return Response({'error': 'invalid credentials'}, status=400)
        return Response(serializer.errors, status=400)

class UserLogoutview(APIView):
       def get(self,request):
            #   request.user.token.delete()
              logout(request)
              return redirect ('login')
              
               
                     

class UpdateCustomerAdminStatus(APIView):
    def post(self, request, customer_id):
        # if not request.user.is_superuser:
        #     return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)

        try:
            user = User.objects.get(id=customer_id)
            if(user.is_staff == True):
                 user.is_staff=False 
                 user.save()
            else:
                  user.is_staff=True
                  user.save()
                 

           
            
            return JsonResponse({'status': 'success', 'message': 'User is now an admin.'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User does not exist.'}, status=404)
        


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer