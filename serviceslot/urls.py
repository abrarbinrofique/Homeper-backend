from django.urls import path,include
from.import views


from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register('book',views.ServiceslotViewset)
router.register('purchase',views.orderview)
urlpatterns = [
    path("",include(router.urls)),
 
    
]
