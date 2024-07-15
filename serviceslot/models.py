from django.db import models
from customer.models import Customer
from service.models import Service

selecttime={
        ('saturday 9AM to 2PM','saturday 9AM to 2PM'),
        ('sunday 2PM to 5PM','sunday 2PM to 5PM'),
        ('Monday 5PM to 8PM','Monday 5PM to 8PM'),

    }

selectstatus={
    ('pending','pending'),
    ('cancel','cancel'),
    ('Done',('Done'))
}


# Create your models here.
class ServiceSlot(models.Model):
    chooce=models.CharField(choices=selecttime, max_length=50)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    service=models.ForeignKey(Service, on_delete=models.CASCADE)
    created_time=models.TimeField(auto_now_add=True)
    service_status=models.CharField(choices=selectstatus, max_length=50,default='pending')


   

