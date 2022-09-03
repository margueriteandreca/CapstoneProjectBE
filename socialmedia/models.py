from django.contrib.auth.models import AbstractUser
from django.db import models


from rest_framework.authtoken.models import Token

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=25)
    avatar = models.ImageField()
    bio = models.CharField(max_length=160, blank=True)
    bio_link = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class UserFollower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    text_content = models.CharField(max_length=255)
    image_content = models.CharField(max_length=255)
    publication_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    text_content = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)




# from django.db import models

# # Create your models here.

# class User(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     username = models.CharField(max_length=16, unique=True)
#     password = models.CharField(max_length=25)
#     avatar = models.CharField(max_length=255, blank=True)
#     bio = models.CharField(max_length=160, blank=True)
#     bio_link = models.CharField(max_length=255, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

# class UserFollower(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     following = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Post(models.Model):
#     text_content = models.CharField(max_length=255)
#     image_content = models.CharField(max_length=255)
#     publication_datetime = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)


# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)


# class Reply(models.Model):
#     text_content = models.CharField(max_length=255)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)


