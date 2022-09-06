from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from socialmedia.serializers import PostSerializer
from .models import User
from socialmedia.models import Post
from .serializers import UserSerializer, FeedUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


@api_view(http_method_names=['GET'])
def user_feed(request):
    following = request.user.following.all()
    serializer = FeedUserSerializer(following, many=True)
    return Response(serializer.data)
        
    
