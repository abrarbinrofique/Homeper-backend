from django.contrib import admin
from  .models import ContactUs
# Register your models here.

class contactadmin(admin.ModelAdmin):
    list_display =['name','phone','email','problems']

admin.site.register(ContactUs,contactadmin)

