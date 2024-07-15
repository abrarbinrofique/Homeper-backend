from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# Register viewsets directly
router.register('', views.CustomerViewsets)


urlpatterns = [
   
    path('login/',views.UserLoginAPIView.as_view(),name='login'),
    path('logout/',views.UserLogoutview.as_view(),name='logout'),
    path('register/',views.UserRegistraitionView.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activate,name="active"),
    path('customers/<int:customer_id>/admin/', views.UpdateCustomerAdminStatus.as_view(), name='make_admin'),
    path('',include(router.urls)),
   
]
