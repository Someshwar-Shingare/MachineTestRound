from django.urls import path
from .import views
urlpatterns = [
               path('log/',views.loginView),
               path('reg/',views.registerView)
]