from django.urls import path 
from rest_framework.routers import SimpleRouter
from .models import User
from . import views 


router = SimpleRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    *router.urls,
    path("feed/", views.user_feed)
    # path("login/", views.login),
    # path("me/", views.remain_logged_in),
    # path("user/<id>", views.show_user)
]
