from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homeView),
    path('about/',views.aboutView),
    path('login/',views.loginView),
    path('reg/',views.registerView),
    path('cont/', views.contactView)

]