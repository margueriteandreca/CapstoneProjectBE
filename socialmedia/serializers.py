from asyncore import read
from email.policy import default
from rest_framework import serializers

from accounts.serializers import FeedUserSerializer, UserSerializer
from .models import Post, Like, Image, Reply

from drf_extra_fields.fields import Base64ImageField


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['post', 'id', 'image']

class UploadedBase64ImageSerializer(serializers.Serializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Image
        fields = ['post', 'id', 'image']

    def create(self, validated_data):  
        image = Image.objects.create(**validated_data)
        return image

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post']


class ReplySerializer(serializers.ModelSerializer):
    user = FeedUserSerializer()
    class Meta:
        model = Reply
        fields = ['id', 'text' , 'user', 'post']

class CreateReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'text' , 'user', 'post']


class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True, default=[])
    images = ImageSerializer(many=True, read_only=True, default=[])

    # https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'publication_datetime', 'likes', 'user', 'like_count', 'images']

    def get_like_count(self, post):
        return post.likes.count()

class CreatePostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True, default=[])
    # images = UploadedBase64ImageSerializer(many=True, read_only=True, default=[])

    class Meta:
        model = Post
        fields = ["id", "text", "publication_datetime", "likes", "user", "is_draft"]

    def create(self, validated_data):  
        post = Post.objects.create(**validated_data)
        return post


class FeedPostSerializer(serializers.ModelSerializer):
    user = FeedUserSerializer()
    likes = LikeSerializer(many=True)
    images = ImageSerializer(many=True)
    replies = ReplySerializer(many=True)
    # reply_user = UserSerializer()


    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'publication_datetime', 'likes', 'like_count', 'images', 'user', 'replies']

    def get_like_count(self, post):
        return post.likes.count()

    # def get_reply_user(self, reply):
    #     return reply.user


# class PostSerializer():
#     id = serializers.IntegerField()
#     user = serializers.SerializerMethodField(method_name="show_user")
#     text_content = serializers.CharField(max_length=255)
#     image_content = serializers.ImageField(method_name="show_replies")
#     likes = serializers.SerializerMethodField(method_name="count_likes")
#     replies = serializers.SerializerMethodField()
#     publication_datetime = serializers.DateTimeField()
#     created_at = serializers.DateTimeField(auto_now_add=True)


#     def show_user(self, post: Post):
#         return post.user

#     def count_likes(self, post: Post):
#         return len(post.likes)

    
#     def show_replies(self, post: Post):
#         return post.replies 
    




# class UserSerializer(): 
#     id = serializers.IntegerField()



# # Feed Photo Serializer
# # need: id, image, text content, publication_date, user attached to post 
# # also number of likes it has - post.likes.length 

