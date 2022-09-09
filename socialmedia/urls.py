from django.urls import path 
from rest_framework.routers import SimpleRouter
from . import views 
from django.conf.urls.static import static
from CapstoneProjectBE import settings


router = SimpleRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    *router.urls,
    path("hello/", views.hello),
    path("new_post/", views.CreatePost.as_view()),
    path("like/", views.LikeAPI.as_view()),
    path("like/<pk>", views.LikeAPI.as_view()),
    path("reply/", views.ReplyAPI.as_view()),
    path("reply/<pk>", views.ReplyAPI.as_view()),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)