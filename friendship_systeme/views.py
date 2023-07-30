from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib import messages
from friendship.models import Friend, Follow, Block ,FriendshipRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import FilteredRelation, Q
from rest_framework import serializers
from django.contrib.auth.models import User



def all_users(request):
    '''all_users = User.objects.exclude(pk=request.user.id)
    
    list_users ={
        'all_users':all_users,
    }'''
    data = {
        "id":1,
    }

    return render(request,'friendship_systeme/all_unread_requests.html')
    

@csrf_exempt
def add_friend(request):
    if request.method == 'POST':
        try:
            other_user=request.POST.get('user_to_add')
            other_user = User.objects.get(pk=other_user)
            Friend.objects.add_friend(request.user,other_user)

            return JsonResponse({'messge':'Add Succes'})

        except:
            return JsonResponse({'messge':'You Can Not ADD This Person','Error':True})


def sent_request(request):
    my_requests = Friend.objects.sent_requests(user=request.user)

    _requests_= {
        'MY_requests':my_requests,
    }

    return render(request,'friendship_systeme/sent_requesets.html',_requests_)


def unread_requests_view(request):
    #all_unread_requests = Friend.objects.unread_requests(user=request.user)#its not working good
    all_unread_requests = FriendshipRequest.objects.filter(to_user=request.user.id)
    #print(FriendshipRequest._meta.get_fields())
    #print(all_unread_requests[0].from_user)
    #take just the person that sends friend invetition
    user_from = list()
    for i in all_unread_requests:
        user_from.append(i.from_user)

    response = {

        'all_unread_requests':user_from
    }
    return render(request , 'friendship_systeme/all_unread_requests.html' , response)
    


@csrf_exempt
def accept(request):
    if request.method =='POST':

        other_user = request.POST.get('usr_id')
        try:
            friend_request = FriendshipRequest.objects.get(from_user=other_user, to_user=request.user.id)
            friend_request.accept()

            return JsonResponse({'messge':f'{request.user.id} and {other_user} are friends now'})
        except:
            return JsonResponse({'messge':'You Can Not Accept not Exicting FriendshipRequest','Error':True})



@csrf_exempt
def reject(request):
    if request.method =='POST':

        other_user = request.POST.get('usr_id')
        try:
            friend_request = FriendshipRequest.objects.get(from_user=other_user, to_user=request.user.id)
            friend_request.delete()

            return JsonResponse({'messge':f'{request.user.id} reject the user {other_user}'})

        except:
            return JsonResponse({'messge':'You Can Not Reject not Exicting FriendshipRequest','Error':True})


        
        
        
        
    

    