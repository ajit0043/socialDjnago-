import json
import requests
from rest_framework import status, permissions, serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import AuthenticationFailed
import datetime
from django.contrib.auth import login, logout, authenticate
# from dj_rest_auth.registration.views import SocialConnectView, SocialLoginView
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, render


# simple endpoint to take the serializer data


def index(request):
    return render(request, "accountss/index.html")


class UserCreationViewSet(APIView):
    # permission class set to be unauthenticated
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"status": "OK", "message": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(ListAPIView):
    serializer_class = UserListSerializer
    queryset = UserModel.objects.all()


class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username", None)
        password = request.data.get("password")
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # it will return token
                return Response(status=status.HTTP_200_OK)
            else:
                return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Credential can't be empty", status=status.HTTP_406_NOT_ACCEPTABLE)


class SendRequestView(APIView):

    def post(self, request):

        try:
            sender = UserModel.objects.get(pk=request.data["sender"])
            receiver = UserModel.objects.get(pk=request.data["receiver"])
            if sender is not None and receiver is not None:
                data = FriendRequestModel.objects.filter(sender_id=sender, receiver_id=receiver)
                if data:
                    return Response("You are in pending", status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    FriendRequestModel.objects.create(sender_id=sender.id, receiver_id=receiver.id)
                return Response("Request sent", status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class FriendRequestView(APIView):
    def get(self, request, pk):
        queryset = FriendRequestModel.objects.filter(sender=pk)
        serializer = FriendRequestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
