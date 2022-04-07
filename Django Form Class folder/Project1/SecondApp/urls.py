from django.urls import path
from .views import loginView,registerView,contactView
urlpatterns = [
                 path('log/',loginView),
                 path('reg/',registerView),
                 path('con/',contactView)
    ]