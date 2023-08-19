from django.urls import path,include
from user_profile.views import ProfileViewSet
 

urlpatterns = [
   path('profile/', ProfileViewSet.as_view({ 'get': 'retrieve', 'put': 'update' })),
  
]
