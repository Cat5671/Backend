from django.urls import path
from gateway.views import pro_req

urlpatterns = [
    path('', pro_req),
]