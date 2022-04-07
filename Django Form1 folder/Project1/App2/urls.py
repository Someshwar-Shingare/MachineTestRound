from django.urls import path
from .views import login1View,register1View
urlpatterns = [
                 path('log1/',login1View),
                 path('reg1/',register1View)
    ]
