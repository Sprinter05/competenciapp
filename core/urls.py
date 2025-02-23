from django.urls import path

from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("profile/<int:uid>/", views.get_user_profile, name="user_profile"),
    path("profile/add_language/", views.add_language, name="add_language"),
    path("profile/add_library/", views.add_library, name="add_library"),
    path("technologies/language/<int:uid>", views.language, name="get_language"),
    path("technologies/library/<int:uid>", views.library, name="get_library"),
    path("search/", views.search, name="search"),
]