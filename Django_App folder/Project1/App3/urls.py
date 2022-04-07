from django.urls import path
from .views import ht7view,ht8view
urlpatterns = [
                 path('h7/',ht7view),
                 path('h8/',ht8view)
                 ]
