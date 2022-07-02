from django.shortcuts import render
from rest_framework import  viewsets
from .models import Link
from .serializers import LinkSerializer

# Create your views here.
class PostListApi(ListApiView):
	queryset=Link.objects.filter(active=True)
	serializer_class= LinkSerializer

class PostCreateApi(CreateApiView):
	queryset=Link.objects.filter(active=True)
	serializer_class= LinkSerializer

class PostDetailApi(RetrieveAPIView):
	queryset=Link.objects.filter(active=True)
	serializer_class= LinkSerializer

class PostUpdateApi(UpdateAPIView):
	queryset=Link.objects.filter(active=True)
	serializer_class= LinkSerializer

class PostDeleteApi(DestroyAPIView):
	queryset=Link.objects.filter(active=True)
	serializer_class= LinkSerializer