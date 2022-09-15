from rest_framework import serializers

from . import models
from socialmedia.models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "username"]

class AllUsersSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    class Meta:
        model = models.User
        fields = ["id", "username", "avatar", "followers"]

    def get_followers(self, obj):
        return FollowersSerializer(obj.user_following.all(), many=True).data
    
class FollowersSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    class Meta:
        model = models.UserFollower
        fields = ("id", "user")

    # def get_user(self, obj):
    #     return FeedUserSerializer(obj.user).data

class ProfileSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        fields = ["id", "first_name", "last_name", "username", "bio", "bio_link", "avatar", "following", "followers"]

    def get_followers(self, obj):
        return FollowersSerializer(obj.user_following.all(), many=True).data


class FeedUserSerializer(serializers.ModelSerializer):
    # def get_posts(self, user): 
    #     posts = Post.objects.filter(user__id=user.id)
    #     serializer = FeedPostSerializer(posts, many=True)
    #     return serializer.data

    # posts = serializers.SerializerMethodField()
    class Meta:
        model = models.User
        fields = ['id', 'username', "avatar"]


class UserFollowerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.UserFollower
        fields = ['id', 'user', "following"]




    