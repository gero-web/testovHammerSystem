from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import login, logout 
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from custom_user.utils import generate_otp


# Create your views here.
@extend_schema(
        description="POST запрос на вход по номеру телефона, также добавляет номер телефона в базу данных",
        responses={200: str},
         examples=[
            OpenApiExample(
                'Example 1',
                description='Для создания\\получения otp введите номер телефона формате +999999',
                value= 'user_phone: string',
            ),
        ],
)
@api_view(['POST'])
def login_otp(request):
    otp = generate_otp.generate()
    user_phone = request.data.get('user_phone', False)
    if not user_phone:
        Response({'msg': 'Please provide phone'}, status=status.HTTP_400_BAD_REQUEST)
    user_model = get_user_model()
    user, _ = user_model.objects.get_or_create(phone=user_phone)
    user.onetimepass = otp
    user.save()
    request.session['user_phone'] = user_phone    
    return Response({'otp': otp}, status=status.HTTP_200_OK)
    
@extend_schema(
        description="POST запрос для ввода otp кода который предоставляет запрос login",
        responses={200: str},
        examples=[
            OpenApiExample(
                'Example 1',
                description='Для получение JWT токена введите otp',
                value= 'otp:string',
            ),
        ],
)   
@api_view(['POST'])
def otp_validation(request):
    
    if 'user_phone' not in  request.session:
        return Response({'msg': 'session expired '}, status=status.HTTP_403_FORBIDDEN) 
    user_phone = request.session['user_phone']
    otp = request.data.get('otp', False)
    print(otp)
    if not otp:
         return  Response({'msg': 'Please provide otp'}, status=status.HTTP_400_BAD_REQUEST)
    user_model = get_user_model()
    user = user_model.objects.get(phone = user_phone)
    
    if int(user.onetimepass) == int(otp):
        refresh =  RefreshToken.for_user(user)
        del request.session['user_phone']
        request.session.modified = True
        return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                },
                status=status.HTTP_200_OK) 
    return Response({'msg': 'otp is not valid'}, status=status.HTTP_400_BAD_REQUEST) 


 