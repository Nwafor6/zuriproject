from django.shortcuts import render
from rest_framework import  viewsets, generics
from links.models import Link
from links.serializers import LinkSerializer

# Create your views here.
class PostListApi(generics.ListApiView):
	queryset=Link.objects.filter(active=True)
	serializer_class= LinkSerializer

class PostCreateApi(generics.CreateApiView):
	queryset=Link.objects.filter(active=True)
	serializer_class= LinkSerializer

class PostDetailApi(generics.RetrieveAPIView):
	queryset=Link.objects.filter(active=True)
	serializer_class= LinkSerializer

class PostUpdateApi(generics.UpdateAPIView):
	queryset=Link.objects.filter(active=True)
	serializer_class= LinkSerializer

class PostDeleteApi(generics.DestroyAPIView):
	queryset=Link.objects.filter(active=True)
	serializer_class= LinkSerializer