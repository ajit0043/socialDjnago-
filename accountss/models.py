from __future__ import unicode_literals
from django.db import models
import uuid
from django.db import models
from django.utils import timezone
from django.db import transaction

from django.contrib.auth.models import AbstractUser


# Create your models here.

class DataLoggerModel(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserModel(AbstractUser):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=False)
    middle_name = models.CharField(max_length=30, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class ProfilePicModel(DataLoggerModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True)
    image = models.FileField(upload_to='profile/images/', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class FriendRequestModel(DataLoggerModel):
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='sender', blank=True, null=True)
    receiver = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='receiver', blank=False)

    def __str__(self):
        return str(self.id)


class FriendModel(DataLoggerModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='current', blank=False)
    friends = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='added_friends', blank=False)

    def __str__(self):
        return str(self.id)
