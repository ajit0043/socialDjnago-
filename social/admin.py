from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(PostModel)
admin.site.register(PostPhotoModel)
admin.site.register(CommentModel)
admin.site.register(ReplayCommentModel)
admin.site.register(CommentReaction)
admin.site.register(ReactionModel)