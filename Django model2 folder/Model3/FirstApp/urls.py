from django.urls import path
from .views import showStudents

urlpatterns = [
                path('show/',showStudents)
              ]