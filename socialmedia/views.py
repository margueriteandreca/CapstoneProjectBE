from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

# Create your views here.
#CONTROLLER - request handler 

@api_view
def say_hello(request):
    return HttpResponse("Hello Marguerite")



@api_view
def all_products(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view
def login(request):
    pass

@api_view 
def remain_logged_in(request):
    pass


@api_view
def show_user(request, id):
    pass
