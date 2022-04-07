from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.testView,name='test'),
    path('signup/', views.signupView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('testview/',views.testView,name='testv'),
    path('fbv/', views.fbView, name='fbv'),
    path('cbv/', views.ClassBasedView.as_view(), name='cbv')

]