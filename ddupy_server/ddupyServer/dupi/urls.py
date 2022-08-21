from django.urls import path, include
from .views import dupicheck

urlpatterns = [
    path("dupicheck/", dupicheck)
]