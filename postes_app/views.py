from django.shortcuts import render
from django.http import JsonResponse
#import models
from .models import Comment , Post , Post_Owner
#import serializers
from .serialzer import Comment_serializer , User_serializer , Post_serialiser
#rest django
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class Comment_Viwe(APIView):

    def get(self , request , format=None):
        #request.data.get('post_id')
        # $ test the errors cases
        try :
            comments = Post.postes.comments_of_post(request.data.get('post_id') ,
                                                     request.data.get('titel') ,
                                                     request.data.get('time_of_pub'))
        except Comment.DoesNotExist : 
            return Response({'messge':'Comments not found ⛔'} ,status = status.HTTP_404_NOT_FOUND)
        except Post.DoesNotExist :
            return Response({'messge':'Post not found ⛔'} ,status = status.HTTP_404_NOT_FOUND) 

        comments = Comment_serializer(comments , many=True)
        '''persons = Post.postes.owner_post(1)
        persons = User_serializer(persons , many = False)'''
        return Response(comments.data , status = status.HTTP_200_OK)
    
    
    def post(self , request , format = None):
        data_serializer = Comment_serializer(data = request.data)

        if data_serializer.is_valid():
            data_serializer.save()
            return Response(data_serializer.data, status=status.HTTP_201_CREATED)
        return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put (self , request ) : 
        comment = Comment.objects.get (id = request.data.get('comment_code:********'))
        comment_serilz = Comment_serializer(instance = comment , data = request.data)

        if comment_serilz.is_valid() : # ❗
            comment_serilz.save()
            return Response ({'message' : 'comment upadated ✔️'}, status = status.HTTP_201_CREATED)
        
        return Response(comment_serilz.errors , status= status.HTTP_400_BAD_REQUEST)
 

    def delete(self , request):
        try : 
            Post.postes.delete_comment( comment_id = request.data.get('comment_id') ,
                                        post_id = request.data.get('post_id') ,
                                        ownerComment_id =  request.data.get('user_commented'))
            return Response({'message': 'comment deleted ✔️'} , status = status.HTTP_200_OK)
        except Comment.DoesNotExist :
            return Response({'message': 'comment not exist ⛔'} , status = status.HTTP_400_BAD_REQUEST)
        

class Users_Poste_View (viewsets.ViewSet) : 
    def post_owner (self, request ):
        #* get the 
        try : 
            owner = Post.postes.owner_post  ( 
                                                post_id = request.data.get('post_id'),
                                                titel = request.data.get('titel') ,
                                                time_pub = request.data.get('time_of_pub')
                                            )
        except Post_Owner.DoesNotExist: 
            return Response({'message': 'owner not exist ⛔'} , status = status.HTTP_404_NOT_FOUND)
        
        owner = User_serializer(owner , many = False)
        return Response(owner.data  , status = status.HTTP_200_OK ) #$ ✔️
    
    
    def uesers_commented ( self , request) : 
        try : 
            persones_commented = Post.postes.persones_commented(
                                                post_id = request.data.get('post_id'),
                                                titel = request.data.get('titel') ,
                                                time_pub = request.data.get('time_of_pub')
            )

        except Comment.DoesNotExist : 
            return Response({'message': 'error of comment exist ⛔'} , status = status.HTTP_404_NOT_FOUND)
        
        persones_commented = User_serializer(persones_commented , many = True)
        return Response(persones_commented.data  , status = status.HTTP_200_OK ) #$ ✔️
        


class Post_view (APIView) :

    def delete (self , request ) : 

        try :
            Post.postes.post_delete(post_id = request.data.get("post****"),
                                    titel = request.data.get("titel"),  
                                    time_pub = request.data.get("time_pub"))

        except Post.DoesNotExist: 
            return Response({'message' : 'Post does not exist make sure that your request mutch api requrements 📛'} , status = status.HTTP_400_BAD_REQUEST)
        except Comment.DoesNotExist: 
            return Response({'message' : 'Comment does not exist make sure that your request mutch api requrements 📛'} , status = status.HTTP_400_BAD_REQUEST)
        except Post_Owner.DoesNotExist: 
            return Response({'message' : 'Post_Owner does not exist make sure that your request mutch api requrements 📛'} , status = status.HTTP_400_BAD_REQUEST)
        
        return Response({'message' : 'Post deleted ✔️'} , status = status.HTTP_200_OK)
    


    def post (self , request ) : 
        serializer = Post_serialiser( data = request.data)

        if serializer.is_valid() :
            serializer.save()
            # $ if the post created than we create the owner
            #// we do it with a function in the Post manager
            Post.postes.create_post_owner ( owner_id =  request.COOKIES , post_id = serializer.data)
            return Response ( status = status.HTTP_201_CREATED)
        
        return Response (status = status.HTTP_400_BAD_REQUEST)


        
        
        

    

    
