from django.urls import path
from .views import addstudentView
urlpatterns = [
                 path('add/',addstudentView)
    ]