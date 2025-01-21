from django.urls import path
from task.views import forms, room


urlpatterns = [
    path('', forms),
    path('room/', room)
]