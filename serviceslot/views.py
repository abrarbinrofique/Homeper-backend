from django.shortcuts import render
from .import models
from .import serializers
from rest_framework import viewsets
from sslcommerz_lib import SSLCOMMERZ
import random 
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

#     def post(self,request):

#         serializer=self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             order=serializer.save()
#             serviceslots=models.ServiceSlot.request.data.get(id=serviceslot_id)
#             payment_response=self.payment(order.id,serviceslots)
#             return Response({
#                 'order': serializer.data,
#                 'payment_response': payment_response
#             }, status=status.HTTP_201_CREATED)


        

      
          


#     def payment(self,pk,ss):
#        order =models.CustomerOrder.objects.get(pk=pk)
       
       

        
#        settings = { 'store_id': 'abgro671e745d23a8c', 'store_pass': 'abgro671e745d23a8c@ssl', 'issandbox': True }
#        sslcz = SSLCOMMERZ(settings)
#        post_body = {}
#        post_body['total_amount'] = 100.26
#        post_body['currency'] = "BDT"
#        post_body['tran_id'] = random(1000,9999)
#        post_body['success_url'] = "your success url"
#        post_body['fail_url'] = "your fail url"
#        post_body['cancel_url'] = "your cancel url"
#        post_body['emi_option'] = 0
#        post_body['cus_name'] =order.name,
#        post_body['cus_email'] =order.email 
#        post_body['cus_phone'] =order.phone
#        post_body['cus_add1'] =order.address 
#        post_body['cus_city'] = "Dhaka"
#        post_body['cus_country'] = "Bangladesh"
#        post_body['shipping_method'] = "NO"
#        post_body['multi_card_name'] = ""
#        post_body['num_of_item'] = 1
#        post_body['product_name'] = "Test"
#        post_body['product_category'] = "Test Category"
#        post_body['product_profile'] = "general"


#        response = sslcz.createSession(post_body) 
#        print(response)
   