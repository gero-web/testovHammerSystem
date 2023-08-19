from django.urls import path
from custom_user.views import otp_validation, login_otp
from rest_framework_simplejwt import views as jwt_views

app_name = 'custom_user'

urlpatterns = [
   path('login/', login_otp, name='login' ),
   path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh' ),
   path('otp_validation/', otp_validation, name='otp_validation')
]
