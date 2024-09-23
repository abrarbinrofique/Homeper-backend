from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# Register viewsets directly
router.register('', views.CustomerViewsets)


urlpatterns = [
    path('userlist/',views.UserViewSet.as_view({'get': 'list'}), name='userlist'),
    path('login/',views.UserLoginAPIView.as_view(template_name='login.html'),name='login'),
    path('logout/',views.UserLogoutview.as_view(),name='logout'),
    path('register/',views.UserRegistraitionView.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activate,name="active"),
    path('makeadmin/<int:customer_id>/', views.UpdateCustomerAdminStatus.as_view(), name='make_admin'),
    path('',include(router.urls))
   
]
