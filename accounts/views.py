from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from socialmedia.serializers import FeedPostSerializer, PostSerializer
from .models import User
from socialmedia.models import Post
from .serializers import ProfileSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


@api_view(http_method_names=['GET'])
def user_feed(request):
    following = request.user.following.all()
    following_ids = following.values_list('id', flat=True)
    posts = Post.objects.filter(user__id__in=following_ids)
    serializer = FeedPostSerializer(posts.order_by("-publication_datetime"), many=True)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def user_profile(request, pk=None):
    if pk is None:
        user_id = request.user.id
    else:
        user_id = pk 
    posts = Post.objects.filter(user__id=user_id)
    post_serializer = PostSerializer(posts.order_by("-publication_datetime"), many=True)
    serializer = ProfileSerializer(User.objects.get(id=user_id))
    return Response(
        {
        "user": serializer.data, 
        "posts": post_serializer.data
        }
    ) 



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
