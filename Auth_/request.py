import requests


#testing the registering api
'''r = requests.post(
    'http://localhost:8000/api/auth/register/',

    data={
      "username": "Ayoub_Hour",
      "password1": "Hour_@2001@",
      "password2": "Hour_@2001@"
  },
)

print(r.json())
'''
#lohin
'''r = requests.post('http://localhost:8000/api/auth/login/',
                  data={
                        "username": "Ayoub_Hour",
                        "password": "Hour_@2001@",
                  }
                  )

print(r.text)'''

#User

'''headers = {
    'Authorization': 'Token 06372ef7c717b61f75df0f5c8020a79598bcda73',
    'Content-type': 'application/json'
}
r = requests.get(
                    'http://localhost:8000/api/auth/user/',
                    headers=headers
                  )

print(r.status_code)
print(r.text)'''

#logout
'''headers = {
    'Authorization': 'Token 06372ef7c717b61f75df0f5c8020a79598bcda73',
}
r = requests.post(
                    'http://localhost:8000/api/auth/logout/',
                    headers=headers
                  )

print(r.status_code)
print(r.json())'''
##############################################  not working
#Register with verfiction email
'''data = {
    "username": "user2",
    "email": "abdellatifhourbro@gmail.com",
    "password1": "complexpassword123",
    "password2": "complexpassword123"
}
r = requests.post(
                    'http://localhost:8000/api/auth/register/',
                    data=data
                  )

print(r.status_code)
print(r.json())

#verify email
data = {
    "key": "user2",
}
r = requests.post(
                    'http://localhost:8000/api/auth/register/verify-email/',
                    data=data
                  )

print(r.status_code)
print(r.json())
'''

#password rest
'''data = {
    "email": "abdellatifhourbro@gmail.com",
}
r = requests.post(
                    'http://localhost:8000/api/auth/password/reset/',
                    data=data
                  )

print(r.status_code)
print(r.json())
'''

'''data = {
      "uid": "h",
      "token": "brl1qw-9b559cd77aca77aa32553618820c61d9",
      "new_password1": "Hour@abdo@@@#",
      "new_password2": "Hour@abdo@@@#",
}
r = requests.post(
                    'http://localhost:8000/api/auth/password/reset/confirm/',
                    data=data
                  )

print(r.status_code)
print(r.json())'''

######################################################
'''data = {
      "new_password1": "Hour@abdo@#",
      "new_password2": "Hour@abdo@#",
      "old_password": "Hour@abdo@@@#"
}
r = requests.post(
                    'http://localhost:8000/api/auth/password/change/',
                    data=data
                  )

print(r.status_code)
print(r.json())'''