from django.db import models
from accounts.models import User
from django.utils.timezone import now


class Post(models.Model):
    text = models.CharField(max_length=255, null=True, blank=True)
    # image_content = models.CharField(max_length=255, null=True, blank=True)
    publication_datetime = models.DateTimeField(default=now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=False)


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=False, upload_to='images')


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ["user", "post"]


class Reply(models.Model):
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
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


