# from django.shortcuts import render
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
from .serializers import LikeSerializer, PostSerializer, CreatePostSerializer, ReplySerializer
from socialmedia import serializers

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class CreatePost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # breakpoint()
        serializer = CreatePostSerializer(data={**request.data, "user": request.user.id })
        if serializer.is_valid():
            post = serializer.save()
            if 'image' in request.data:
                Image.objects.create(image=request.data['image'], post=post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        serializer = ReplySerializer(data={**request.data, "user": request.user.id })
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




# @api_view
# def all_products(request):
#     queryset = Post.objects.all()
#     serializer = PostSerializer(queryset, many=True)
#     return Response(serializer.data)


# @api_view
# def login(request):
#     pass

# @api_view 
# def remain_logged_in(request):
#     pass


# @api_view
# def show_user(request, id):
#     pass


# # function to fetch user posts for feed
# # find current logged in user 
# # feed_users = user.following
# # feed_users.posts - render in order of publication_date 


# @api_view
# def increment_likes(request, id):
#     user = "??"
#     post = Post.objects.get(pk = id)
#     Like.create(user = user, post = post)