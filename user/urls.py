from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.LogOut, name="logout"),
    path("change_password/", views.change_password, name="change_password"),
    path("set_password/", views.set_password, name="set_password"),
]
