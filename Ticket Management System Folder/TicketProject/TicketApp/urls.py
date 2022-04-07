from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),

    path('create_order/<str:pk>/', views.createTicket, name="create_ticket"),
    path('update_order/<str:pk>/', views.updateTicket, name="update_ticket"),
    path('delete_order/<str:pk>/', views.deleteTicket, name="delete_ticket"),
]