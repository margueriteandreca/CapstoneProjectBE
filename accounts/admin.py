from django.contrib import admin
from .models import User, UserFollower
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
