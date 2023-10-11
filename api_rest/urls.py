from django.urls import path
from .views import get_users, get_by_nick, user_manage

urlpatterns = [
    path("", get_users, name="get_users_url"),
    path("user/<str:nick>", get_by_nick),
    path("data/", user_manage)
]
