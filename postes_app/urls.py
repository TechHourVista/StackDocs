from django.urls import path
from .views import Comment_Viwe , Users_Poste_View , Post_view


urlpatterns = [
    path("comments_of_post/",Comment_Viwe.as_view() , name="comments_of_post"),
    path("owner_of_post/",  Users_Poste_View.as_view({'get' : 'post_owner'}), name="owner_of_post"),
    path("users_that_commented_this_post/",  Users_Poste_View.as_view({'get' : 'uesers_commented'}), name="users_that_commented_this_post"),
    path("post_rout/" , Post_view.as_view() , name = "post_rout") ,
]
