from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from socialmedia.serializers import FeedPostSerializer, PostSerializer
from .models import User
from socialmedia.models import Post
from .serializers import ProfileSerializer, UserSerializer, UserFollowerSerializer, AllUsersSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from datetime import datetime


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AllUsersSerializer
    permission_classes = [IsAuthenticated]


@api_view(http_method_names=['GET'])
def user_feed(request):
    following = request.user.following.all()
    following_ids = following.values_list('id', flat=True)
    posts = Post.objects.filter(user__id__in=following_ids)
    now = datetime.now()
    published_posts = posts.filter(publication_datetime__lte=now)
    filtered_posts = filter(lambda post: post.is_draft == False, published_posts.order_by("-publication_datetime"))
    serializer = FeedPostSerializer(filtered_posts, many=True)
    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def user_profile(request, pk=None):
    if pk is None:
        user_id = request.user.id
    else:
        user_id = pk 
    posts = Post.objects.filter(user__id=user_id)
    now = datetime.now()
    published_posts = posts.filter(publication_datetime__lte=now)
    filtered_posts = filter(lambda post: post.is_draft == False, published_posts.order_by("-publication_datetime"))
    post_serializer = PostSerializer(filtered_posts, many=True)
    serializer = ProfileSerializer(User.objects.get(id=user_id))
    return Response(
        {
        "user": serializer.data, 
        "posts": post_serializer.data
        }
    ) 

@api_view(http_method_names=['GET'])
def user_drafts(request):
    user_id = request.user.id
    posts = Post.objects.filter(user__id=user_id)
    serializer = PostSerializer(filter(lambda post: post.is_draft == True, posts.order_by("-publication_datetime")), many=True)
    return Response(serializer.data) 

@api_view(http_method_names=['GET'])
def scheduled_posts(request):
    user_id = request.user.id
    posts = Post.objects.filter(user__id=user_id)
    now = datetime.now()
    future_posts = posts.filter(publication_datetime__gt=now)
    filtered_posts = filter(lambda post: post.is_draft == False, future_posts.order_by("-publication_datetime"))
    serializer = PostSerializer(filtered_posts, many=True)
    return Response(serializer.data) 

@api_view(http_method_names=['DELETE'])
def delete_user(request):
    user = request.user
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['PATCH'])
def edit_user(request): 
    user = request.user
    serializer = ProfileSerializer(user, request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['POST'])
def add_follower(request): 
    user = request.user
    serializer = UserFollowerSerializer(data={**request.data, "user": user.id})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)