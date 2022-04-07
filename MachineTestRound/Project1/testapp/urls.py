from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homeView,name='home'),
    path('show/',views.showBooksView,name='show'),
    path('add/',views.addBooksView,name='add'),
    path('update/<int:id>/',views.updateBookView,name='update'),

]