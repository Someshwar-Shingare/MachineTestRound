from django.urls import path
from .views import loginView,registerView
urlpatterns = [
                 path('log/',loginView),
                 path('reg/',registerView)


                 ]