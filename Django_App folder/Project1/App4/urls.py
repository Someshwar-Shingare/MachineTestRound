from django.urls import path
from .views import user1,user2,user3,empviews
urlpatterns = [
                 path('us1/',user1),
                 path('us2/',user2),
                 path('us3/',user3),
                 path('e/',empviews)
]