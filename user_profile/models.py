from django.db import models
from django.contrib.auth import get_user_model


user_model = get_user_model()

# Create your models here.
class Profile(models.Model):
    
    user = models.OneToOneField(user_model, verbose_name=("user"), on_delete=models.CASCADE)
    someone_invite = models.CharField(max_length=6, blank=True, null=True)
    
    
