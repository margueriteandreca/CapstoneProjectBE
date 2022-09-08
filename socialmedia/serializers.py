from rest_framework import serializers

from accounts.serializers import FeedUserSerializer
from .models import Post, Like, Image, Reply


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['post', 'id', 'image']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post']


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'text' , 'user', 'post']


class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True)
    images = ImageSerializer(many=True)

    # https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'publication_datetime', 'likes', 'user', 'like_count', 'images']

    def get_like_count(self, post):
        return post.likes.count()

class FeedPostSerializer(serializers.ModelSerializer):
    user = FeedUserSerializer()
    likes = LikeSerializer(many=True)
    images = ImageSerializer(many=True)
    # replies = ReplySerializer(many=True)

    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'publication_datetime', 'likes', 'like_count', 'images', 'user']

    def get_like_count(self, post):
        return post.likes.count()



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

