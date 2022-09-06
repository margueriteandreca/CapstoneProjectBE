from rest_framework import serializers

from socialmedia.serializers import FeedPostSerializer

from . import models
from socialmedia.models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "username"]
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', "bio", "bio_link", "avatar"]

class FeedUserSerializer(serializers.ModelSerializer):
    def get_posts(self, user): 
        posts = Post.objects.filter(user__id=user.id)
        serializer = FeedPostSerializer(posts, many=True)
        return serializer.data

    posts = serializers.SerializerMethodField()
    class Meta:
        model = models.User
        fields = ['id', 'username', "avatar", "posts"]





    