from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from random import randrange
from django.db import models


def random_string():
    return str(randrange(100_000, 999_999))
# Create your models here.
class CustomUserManager(BaseUserManager):
    
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError('The user must have a phone number.')
        
        if not password:
            raise ValueError('The user must have a password.')
        
        user = self.model(phone=phone)
        user.set_unusable_password()  
        user.is_staff=False
        user.is_admin=False
        user.is_active=True
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, phone, password=None):
        if not phone:
            raise ValueError('The user must have a phone number.')
        
        if not password:
            raise ValueError('The user must have a password.')
        
        user = self.create_user(phone, password=password)
        user.set_password(password)
        user.is_staff=True
        user.is_admin=True
        user.save(using=self.db)
        return user
     
     
     
class User(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', \
                  message ="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    invate = models.CharField(max_length=6, default=random_string )
    name  = models.CharField(max_length=20, blank=True, null=True)
    onetimepass = models.CharField(max_length=9, blank=True, null=True)
     
    first_login = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'phone'
    
    def __str__(self) -> str:
        return self.phone
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    
     
 