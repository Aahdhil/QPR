# qpr_app/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def sync_user_profile(sender, instance, created, **kwargs):
    """
    Signal only ENSURES profile exists.
    DOES NOT create user.
    DOES NOT override manual registration.
    """
    UserProfile.objects.get_or_create(
        user=instance,
        defaults={
            'employee_code': instance.username,
            'role': 'user',
            'profile_updated': False
        }
    )
