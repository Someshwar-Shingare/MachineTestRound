from django.urls import path
from . import views

urlpatterns = [
    path('ho/',views.homeView),
    path('ab/',views.aboutView),
    path('log/',views.loginView),
    path('reg/',views.registerView),
    path('cont/', views.contactView),
    path('ba/',views.baseView)

]