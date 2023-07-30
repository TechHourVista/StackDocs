#import models
from .models import Comment ,Post
from django.contrib.auth.models import User

#import model serializers
from rest_framework import serializers



class Comment_serializer(serializers.ModelSerializer):
    class Meta:
        model =  Comment

        fields = ['id' , 'user_comment' , 'post_comment' , 'text']




class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'username']


class Post_serialiser(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id' , 'titel' , 'time_pub' ,'text']

        