from django.contrib import admin

# Register your models here.
from .models import Service,ReviewModel

from django.db.models import Avg

class ServiceAdmin(admin.ModelAdmin):
    list_display=['Name','price','average_rating']

    def average_rating(self, obj):
       
        average_ratting = ReviewModel.objects.filter(service=obj).aggregate(Avg('ratting'))['ratting__avg']
        return round(average_ratting, 2) if average_ratting else None




admin.site.register(Service,ServiceAdmin)
admin.site.register(ReviewModel)