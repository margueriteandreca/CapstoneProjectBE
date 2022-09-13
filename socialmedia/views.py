# from django.shortcuts import render
from ast import For
from re import I
from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from rest_framework.decorators import api_view, APIView
# from rest_framework import status
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from accounts.models import User, UserFollower
from .models import Post, Like, Reply, Image
from .serializers import LikeSerializer, PostSerializer, CreatePostSerializer, CreateReplySerializer, UploadedBase64ImageSerializer
from socialmedia import serializers

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class CreatePost(APIView):
    permission_classes = [IsAuthenticated]
    # parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        serializer = CreatePostSerializer(data={**request.data, "user": request.user.id })
        if serializer.is_valid():
            post = serializer.save()
            if 'image' in request.data:
                my_image = UploadedBase64ImageSerializer(data={"image": request.data['image']})
                if my_image.is_valid():
                    my_image.save(post=post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, format=None):
        pass

class LikeAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = LikeSerializer(data={**request.data, "user": request.user.id })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, format=None, *args, **kwargs):
        pk = self.kwargs['pk']
        like = Like.objects.get(id=pk)
        if like.user.id is request.user.id: 
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return  Response(status=status.HTTP_400_BAD_REQUEST) 

class ReplyAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreateReplySerializer(data={**request.data, "user": request.user.id })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, format=None, *args, **kwargs):
        pk = self.kwargs['pk']
        reply = Reply.objects.get(id=pk)
        if reply.user.id is request.user.id: 
            reply.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return  Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(http_method_names=['GET'])
def hello(request):
    return Response(
        {
            'user': {'id': request.user.id}

        }
    ) 