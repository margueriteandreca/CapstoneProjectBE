from django.contrib import admin

# Register your models here.
from . import models
from accounts.models import UserFollower

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Reply)
class ReplyAdmin(admin.ModelAdmin):
    pass

