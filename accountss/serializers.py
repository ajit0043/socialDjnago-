from rest_framework import serializers
from .models import *


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'password', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'write_only': False}
        }

    def validated_data(self, data):
        try:
            email = data.get("email", None)
            if email:
                if UserModel.objects.filter(email=data["email"]).exists():
                    raise serializers.ValidationError({
                        "Email": "Email is already in use. Try with another email"
                    })
        except:
            pass
        return super.validate(data)

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance= self.Meta.model(**validated_data)
        instance.is_active = False
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['first_name', 'middle_name', 'last_name', 'email']


class LoginSerializer(serializers.Serializer):
    class Meta:
        username = serializers.EmailField()
        password = serializers.CharField()


class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicModel
        fields = '__all__'


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequestModel
        fields = '__all__'


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendModel
        fields = '__all__'
