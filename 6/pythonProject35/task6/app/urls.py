from django.urls import path
from app.views import process_request

urlpatterns = [
    path('', process_request),
]
