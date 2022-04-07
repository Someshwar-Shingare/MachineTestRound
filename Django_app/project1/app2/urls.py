from django.urls import path
from .views import view3,view4

urlpatterns = [
    path('v3/',view3),
    path('v4/',view4)
    ]
