from django.urls import path
from .views import ht4view,ht5view,ht6view
urlpatterns = [
                 path('h4/',ht4view),
                 path('h5/',ht5view),
                 path('h6/',ht6view)
                 ]
