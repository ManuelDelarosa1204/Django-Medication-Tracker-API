from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.utils.text import slugify
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        slug = slugify(self.username)
        return super(User, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.username

    class Meta:
        indexes = [
            models.Index(fields=["username"], name="user_username_idx"),
            models.Index(fields=["email"], name="user_email_idx"),
        ]


#  Assign DRF Token on user creation
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
