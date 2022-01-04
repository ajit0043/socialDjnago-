from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserModel)
admin.site.register(ProfilePicModel)
admin.site.register(FriendRequestModel)
admin.site.register(FriendModel)