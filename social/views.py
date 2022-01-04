from re import L
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, generics
# Create your views here.


class CreatePostView(APIView):
    def post(self, request):
        img = request.data.get('images', None)
        if img:
            # it may cause any error => Plabon Vai
            pic_serilizer = PostPhotoSerializer(request.data["images"])

        request.data.pop("images")
        serilizer = PostSerializer(request.data)
        if img and serilizer:
            if serilizer.is_valid() and pic_serilizer.is_valid():
                serilizer.save()
        elif img:
            if pic_serilizer.is_valid():
                pic_serilizer.save()
        else:
            serilizer.save()
        return Response(status=status.HTTP_201_CREATED)
    


class CreateCommentView(generics.ListCreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    # def post(self, request):
    #     serializer = CommentSerializer(request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateCommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = CommentSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class ListCreateReplayView(generics.ListCreateAPIView):
    queryset = ReplayCommentModel.objects.all()
    serializer_class = ReplayCommentSerializer

class UpdateRetrieveDestroyReplayView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReplayCommentModel.objects.all()
    serializer_class = ReplayCommentSerializer

class ListCreateCommentReactionView(generics.ListCreateAPIView):
    queryset = CommentReaction.objects.all()
    serializer_class = CommentReactionSerializer


class UpdateRetrieveDestroyCommentReactionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentReaction.objects.all()
    serializer_class = CommentReactionSerializer