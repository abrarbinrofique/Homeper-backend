from django.urls import path,include
from.import views


from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('list',views.ServiceViewsets)

router.register('review',views.ReviewViewsets)


urlpatterns = [
 
    path("",include(router.urls)),
    
]
