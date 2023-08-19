from drf_spectacular.utils import extend_schema 
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from user_profile.serializers import profile_serializer
from user_profile.models import Profile
 

# Create your views here.
class ProfileViewSet(ModelViewSet):
    
    serializer_class  = profile_serializer.ProfileSerializer
    authentication_classes = [TokenAuthentication,JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = [ 'get', 'put']
    
      
    def get_object(self):
        return Profile.objects.get(user = self.request.user)
    
    @extend_schema(
        description="GET запрос на профиль пользователя",
        
    )
    def retrieve(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = profile_serializer.ProfileSerializer(data,   )
        return Response(serializer.data)
    
    @extend_schema(
        description="""put запрос на профиль изменения профиля пользователя  
            обязательным параметром является someone_invite,  параметры users и invate являются не изменяемыми и не обезательными"""
    )
    def update(self, request, *args, **kwargs):
        instance = self.get_object() 
        serializer = profile_serializer.ProfileSerializer(data=request.data, instance=instance)
        if serializer.is_valid( raise_exception=True):
            user_model = get_user_model()
            someone_invite = serializer.validated_data.get('someone_invite')
            exists = user_model.objects.filter(invate = someone_invite).exists()
            if not exists:
                return Response({'msg': 'Invate not found' },status=status.HTTP_404_NOT_FOUND) 
            instance.name =  serializer.validated_data.get('name')
            instance.someone_invite = someone_invite
            instance.save()
            return Response({'msg': 'Update' },status=status.HTTP_200_OK)
        return Response({'msg': 'Error' },status=status.HTTP_400_BAD_REQUEST)
    