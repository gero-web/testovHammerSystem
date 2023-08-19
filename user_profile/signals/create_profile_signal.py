from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from user_profile.models import Profile


user_model = get_user_model()

@receiver(post_save, sender=user_model)
def create_profile(sender, instance, **kwargs):
    print(instance)
    Profile.objects.update_or_create(user=instance)