from django.urls import path
from .views import *

app_name = "social"
urlpatterns = [
    path("login", Login.as_view(), name="login"),
    path("register", Register.as_view(), name="register"),
    path("", Home.as_view(), name="home"),
    path("logout", Logout.as_view(), name="logout"),
]