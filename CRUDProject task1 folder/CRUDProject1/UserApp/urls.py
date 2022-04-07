from django.urls import path
from . import views
urlpatterns = [
    path('test/',views.testView,name='test'),
    path('register/',views.registerView,name='register'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout')
]