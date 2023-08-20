from rest_framework  import serializers
from django.contrib.auth import get_user_model
from user_profile.models import Profile 


user_model = get_user_model()

 

class ProfileSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(source='user.name', required=False)
    phone = serializers.CharField(source='user.phone',required=False )
    invate = serializers.CharField(source='user.invate', required=False )
    users = serializers.SerializerMethodField( required=False  )
    
    
    def get_users(self, obj):
        data =  Profile.objects.filter(someone_invite=obj.user.invate)
        serializer = ProfileSerializer(data=data, many=True)
        serializer.is_valid()
        return serializer.data
    
    
    class Meta:
        model = Profile
        read_only_fields = ('invate', 'users')
       
        fields = ['name', 'phone', 'invate', 'someone_invite', 'users']