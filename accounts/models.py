from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField()
    bio = models.TextField(max_length=160, blank=True, null=True)
    bio_link = models.URLField(max_length=200, blank=True, null=True)
    following = models.ManyToManyField(
        "self", 
        through = 'UserFollower',
        symmetrical = False,
        through_fields=("user", "following"),
        related_name="following_set"
    )

    

class UserFollower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_followers")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_following")
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ["user", "following"]

        
