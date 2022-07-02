from rest_framework import serializers
# from .models import Post
from .models import Link

# class PostSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=Post
# 		fields="__all__"

class LinkSerializer(serializers.ModelSerializer):
	class Meta:
		model=Link
		fields="__all__"