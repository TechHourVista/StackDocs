from  dj_rest_auth.registration.views import RegisterView
from django.urls import path

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import (
                                        LoginView,
                                        LogoutView,
                                        UserDetailsView ,
                                )
#viwes
from .views import sign_up


urlpatterns = [
    path("signup/", sign_up, name="signup"),
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),


]