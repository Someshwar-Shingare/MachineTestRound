from django.urls import path
from .views import view5,view6

urlpatterns = [
    path('v5/',view5),
    path('v6/',view6)
    ]
