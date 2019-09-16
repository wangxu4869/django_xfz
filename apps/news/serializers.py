from rest_framework import serializers
from .models import NewsCategory,News,Comment,Banner
from apps.xfzauth.serializerrs import UserSerializer

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=NewsCategory
        fields=['id','name']


class NewsSerializer(serializers.ModelSerializer):
    category=NewsCategorySerializer()
    author=UserSerializer()
    class Meta:
        model=News
        fields=['id','title','desc','thumbnail','pub_time','category','author']

class CommentSerializer(serializers.ModelSerializer):
    author=UserSerializer()
    class Meta:
        model=Comment
        fields=['id','content','pub_time','author']

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields=['id','image_url','priority','link_to']