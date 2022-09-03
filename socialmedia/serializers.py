from rest_framework import serializers
from .models import Post


class PostSerializer():
    id = serializers.IntegerField()
    user = serializers.SerializerMethodField(method_name="show_user")
    text_content = serializers.CharField(max_length=255)
    image_content = serializers.ImageField(method_name="show_replies")
    likes = serializers.SerializerMethodField(method_name="count_likes")
    replies = serializers.SerializerMethodField()
    publication_datetime = serializers.DateTimeField()
    created_at = serializers.DateTimeField(auto_now_add=True)


    def show_user(self, post: Post):
        return post.user

    def count_likes(self, post: Post):
        return len(post.likes)

    
    def show_replies(self, post: Post):
        return post.replies 
    




class UserSerializer(): 
    id = serializers.IntegerField()



# Feed Photo Serializer
# need: id, image, text content, publication_date, user attached to post 
# also number of likes it has - post.likes.length 

