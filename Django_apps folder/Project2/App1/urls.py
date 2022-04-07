from django.urls import path
from .views import empviews
urlpatterns = [
                 path('e/',empviews)
]