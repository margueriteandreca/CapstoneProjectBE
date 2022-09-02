from django.urls import path 
from . import views 

urlpatterns = [
    path("hello/", views.say_hello),
    path("login/", views.login),
    path("me/", views.remain_logged_in),
    path("user/<id>", views.show_user)
]

