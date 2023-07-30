import requests
import uuid


################### $ for testing the apis that is related to post and comments ####################################
## Get
'''headers = {
    'token':str(uuid.uuid1())

}
data = {
    'post_id':2,
    'titel': 'ffffffffffffffffff', 
    'time_of_pub':'15:20:20.377643',
}
r = requests.get('http://127.0.0.1:8000/post/comments_of_post/' , headers=headers , data = data)

print(r.json())

'''
# post 
'''headers = {
    'token':str(uuid.uuid1()) , 

}
data = {
    'post_comment':1 ,
    'user_comment':18,
    'text' : 'first place 👍'
}
r = requests.post('http://127.0.0.1:8000/post/comments_of_post/' , headers=headers , data = data)
print(r.status_code)
print(r.json().get('id'))'''


# put 
'''headers = {
    'token':str(uuid.uuid1()) , 

}
data = {
    'comment_code:********':3,
    'post_comment':1 ,
    'user_comment':18,
    'text' : 'first place 🥇'
}
r = requests.put('http://127.0.0.1:8000/post/comments_of_post/' , headers=headers , data = data)
print(r.status_code)
print(r.json().get('message'))'''
#Delete
'''headers = {
    'token':str(uuid.uuid1())

}
data = {
    'comment_id':3,
    'post_id':1 ,
    'user_commented':18,

}
r = requests.delete('http://127.0.0.1:8000/post/comments_of_post/' , headers=headers , data = data)

print(r.text)'''


############################### ? api related to post and User ############################
#$ get the post owner 

'''data = {
    'post_id':1,
    'titel': 'jam3a dyl mohmmedia', 
    'time_of_pub':'16:39:14.739626',
}
r = requests.get('http://127.0.0.1:8000/post/owner_of_post/' , data = data )
print(f'status_code: {r.status_code}')
print(r.json())'''
#$ get the users that commented this post 
'''data = {
    'post_id':1,
    'titel': 'jam3a dyl mohmmedia', 
    'time_of_pub':'16:39:14.739626',
}
r = requests.get('http://127.0.0.1:8000/post/users_that_commented_this_post/' , data = data )
print(f'status_code: {r.status_code}')
print(r.json())'''






#####################?######################## requests related to the post like deleteing a post and so on etc ...
#$ deleting a post
'''data = {
    'post****':  7,
    'titel': "gogogogo",
    'time_pub' : "12:58:18.175676"
}

r = requests.delete("http://127.0.0.1:8000/post/post_rout/" , data = data)
print(r.status_code)
print(r.json())'''

#$ post created
'''data = {
    "titel" : "media shcool",
    "text" : "#############################",
}
cookies = {"unique_id" : str(uuid.uuid1()) , "id" : str(1) ,"user_name" : "lasthour" , "date_joined" : "2023-06-23 14:36:33.240922"}

r = requests.post ("http://127.0.0.1:8000/post/post_rout/" , data = data ,cookies = cookies)
print(r.status_code)'''