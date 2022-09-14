from django.urls import path 
from rest_framework.routers import SimpleRouter
from .models import User
from . import views 


router = SimpleRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    *router.urls,
    path("feed/", views.user_feed),
    path("profile/", views.user_profile),
    path("profile/drafts/", views.user_drafts),
    path("profile/<pk>", views.user_profile),
    path("profile/edit/", views.edit_user),
    path("profile/delete/", views.delete_user),
    path("drafts/", views.user_drafts),
    path("scheduled/", views.scheduled_posts)
]
