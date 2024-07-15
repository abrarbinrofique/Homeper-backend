from django.contrib import admin
from .models import ServiceSlot

# Register your models here.


class adminserviceslot(admin.ModelAdmin):
    list_display=['customer','service','created_time','chooce']


    def customer(self,obj):
        return self.customer.user.first_name
    

    


admin.site.register(ServiceSlot,adminserviceslot)
