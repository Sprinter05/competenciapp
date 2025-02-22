from django.urls import path

from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("search/", views.search, name="search"),
]