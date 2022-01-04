import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
from accountss.models import *

# from social_media.accountss.models import *


class PostModel(DataLoggerModel):
    post = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class PostPhotoModel(DataLoggerModel):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, blank=False, null=False)
    picture = models.FileField(upload_to='Post/images', blank=False, null=False)

    def __str__(self):
        return str(self.id)


class CommentModel(DataLoggerModel):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, blank=False, null=False)
    comment = models.TextField(max_length=1000, blank=False, null=False)
    commenter = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post.id)


class ReplayCommentModel(DataLoggerModel):
    comment = models.ForeignKey(CommentModel, on_delete=models.CASCADE)
    replies = models.TextField(max_length=1000, blank=False, null=False)
    replier = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class CommentReaction(DataLoggerModel):
    comment = models.ForeignKey(CommentModel, on_delete=models.CASCADE)
    like = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    total = models.IntegerField(default=0)
    reactor = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class ReactionModel(DataLoggerModel):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, blank=False)
    like = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    total = models.IntegerField(default=0)
    reactor = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post.id)
