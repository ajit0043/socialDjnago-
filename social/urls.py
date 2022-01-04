from os import name
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('create/', views.CreatePostView.as_view(), name='create'),
    path('comment/', views.CreateCommentView.as_view(), name='comment'),
    path('comment/<uuid:pk>/', views.UpdateCommentView.as_view(), name='update-comment'),
    path('replay/', views.ListCreateReplayView.as_view(), name='create-replay'),
    path('replay/<uuid:pk>/', views.UpdateRetrieveDestroyReplayView, name='update-replay'),
    path('reaction/', views.ListCreateCommentReactionView.as_view(), name='reaction'),
    path('reaction/<uuid:pk>/', views.UpdateRetrieveDestroyCommentReactionView.as_view(), name='update-reaction')

]
