from django.urls import path
from .views import append_client_api

urlpatterns = [
    path('', append_client_api)
]
