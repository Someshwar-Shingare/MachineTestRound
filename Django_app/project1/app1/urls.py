from django.urls import path
from .views import view1,view2

urlpatterns = [
    path('v1/',view1),
    path('v2/',view2)
]