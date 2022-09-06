# from django.shortcuts import render
from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from rest_framework.decorators import api_view
# from rest_framework import status
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import User, UserFollower
from .models import Post, Like
from .serializers import PostSerializer
from socialmedia import serializers


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


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