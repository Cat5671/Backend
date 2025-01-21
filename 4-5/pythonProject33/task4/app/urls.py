from django.urls import path

from . import views


urlpatterns = [
    path("", views.log),
    path("registration/", views.register),
    path("profile/", views.profile),
    path("registration/<slug:sl>", views.profile),
    path("profile/<slug:sl>", views.profile),
]