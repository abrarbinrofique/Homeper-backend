from django.shortcuts import render
from .import models
from .import serializers
from rest_framework import viewsets
from sslcommerz_lib import SSLCOMMERZ
import random 
from rest_framework.decorators import action,api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
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


class orderview(viewsets.ModelViewSet):

    queryset=models.customerorderinfo.objects.all()
    serializer_class=serializers.ordersinfoseralizer
    

    @action(detail=True, methods=['post'])
    def post(self,request,pk):
        
        serializer=self.get_serializer(data=request.data)
        
        if serializer.is_valid():
          order=serializer.save()
          serviceslots=models.ServiceSlot.objects.get(pk=pk)
          if order.payment_amount>=serviceslots.main_payment:
            
            
            payment_response=self.payment(order.id,pk)
            if 'payment_url' in payment_response:
                    return Response({
                        'order': serializer.data,
                        'payment_url': payment_response['payment_url']
                    }, status=status.HTTP_201_CREATED)
          else:
             return Response({
                        "error": "Your payment amount is not enough to buy the service."
                    }, status=status.HTTP_400_BAD_REQUEST)
    

    def list(self,request):
       orders=models.customerorderinfo.objects.all()
       lists=self.get_serializer(orders,many=True)
       return Response({
                      "orders": lists.data
                    }, status=status.HTTP_200_OK)



        

      
    def payment(self,pk,ss):
       
       order =models.customerorderinfo.objects.get(pk=pk) 
       print(order)  
       settings = { 'store_id': 'abgro671e745d23a8c', 'store_pass': 'abgro671e745d23a8c@ssl', 'issandbox': True }
       sslcz = SSLCOMMERZ(settings)
      
       post_body = {
       'total_amount' : order.payment_amount,
       'currency': "BDT",
       'tran_id' : random.randint(1000, 9999),
       'success_url': f"https://homeper-backend.vercel.app/serviceslot/purchase/{ss}/paymentsuccess/",
       'fail_url' : "https://homeper-backend.vercel.app/serviceslot/purchase/paymentfailed/",
       'cancel_url' : "https://homeper-backend.vercel.app/serviceslot/purchase/paymentfailed/",
       'emi_option' : 0,
       'cus_name' :order.name,
       'cus_email' :order.email, 
       'cus_phone' :order.phone,
       'cus_add1' :order.address, 
       'cus_city' : "Dhaka",
       'cus_country' : "Bangladesh",
       'shipping_method' : "NO",
       'multi_card_name' : "",
       'num_of_item' : 1,
       'product_name' : "Test",
       'product_category' : "Test Category",
       'product_profile' : "general",
       }
       

       response = sslcz.createSession(post_body)

       if 'GatewayPageURL' in response:
            return {'payment_url': response['GatewayPageURL']}
       else:
            return {'error': 'Payment session could not be created'}
       

    @action(detail=True, methods=['get','post'])
    def paymentsuccess(self,request,pk,):
        serviceslots=models.ServiceSlot.objects.get(pk=pk)
        if serviceslots.service_status!='paid':
          serviceslots.service_status='paid'
          serviceslots.save()
        return redirect('https://abrarbinrofique.github.io/Homper-frontend/')

    @action(detail=True, methods=['get','post'])
    def cod(self,request,pk,):
        serviceslots=models.ServiceSlot.objects.get(pk=pk)
        if serviceslots.service_status!='Cash on delivery':
          serviceslots.service_status='Cash on delivery'
          serviceslots.save()
         
        return redirect('https://abrarbinrofique.github.io/Homper-frontend/bookiingslip.html')
    

    @action(detail=False, methods=['get', 'post'])
    def paymentfailed(self, request):

        return redirect('https://abrarbinrofique.github.io/Homper-frontend/bookiingslip.html')
    
    


    @action(detail=False, methods=['get', 'post'])
    def paymentfailed(self, request):

        return redirect('https://abrarbinrofique.github.io/Homper-frontend/bookiingslip.html')
    


# http://127.0.0.1:8000/serviceslot/purchase/17/post/