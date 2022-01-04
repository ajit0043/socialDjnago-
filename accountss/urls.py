from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
# router.register('user', UserCreationViewSet, basename='account_apis')

urlpatterns = [
    path('', index, name="index"),
    path('user/create/', UserCreationViewSet.as_view(), name='create_user'),
    path('user/login/', LoginView.as_view()),
    path('accounts/', include('allauth.urls')),
    path('user/login/', LoginView.as_view()),
    path('user/list/', UserList.as_view()),
    path('user/sent/request/', SendRequestView.as_view()),
    path('user/friend/request/<str:pk>/', FriendRequestView.as_view()),

]
