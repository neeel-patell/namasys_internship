from .views import *
from django.urls import path

urlpatterns = [
    path("", index, name="login"),
    path("logout", logout, name="logout"),
    path("signup", signup, name="signup"),
    path("details", user_details, name="details"),
    path("details/<int:id>", get_user_details, name="get_user_details"),
    path("edit/details/", edit_user_details, name="edit_user_details"),
    path("delete/details/<int:id>", delete_user_details, name="delete_user_details"),
]
