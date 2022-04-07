from django.urls import path
from .import views
urlpatterns = [
               path('ho/',views.homeView),
               path('ab/',views.aboutView)
        ]