from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'


class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhotoModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'


class ReplayCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplayCommentModel
        fields = '__all__'


class CommentReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReaction
        fields = '__all__'


class ReactionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReactionModel
        fields = '__all__'
