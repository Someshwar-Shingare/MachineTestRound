from django.urls import path
from .views import user1view,user2view,user3view,userview
urlpatterns = [
                 path('u1/',user1view),
                 path('u2/',user2view),
                 path('u3/',user3view),
                 path('u/', userview)
]

