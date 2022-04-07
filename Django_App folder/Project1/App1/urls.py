from django.urls import path
from .views import loginview,templateview,ht1view,ht2view,ht3view
urlpatterns = [
                 path('log/',loginview),
                 path('tem/',templateview),
                 path('h1/',ht1view),
                 path('h2/',ht2view),
                 path('h3/',ht3view)
                 ]