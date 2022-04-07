from django.urls import path
from . import views

urlpatterns = [
    path('ho/',views.HomePageView),
    path('f/',views.FirstPageView),
    path('s/',views.SecondPageView),
    path('t/',views.ThirdPageView),
    path('fo/', views.FourthPageView),
    path('fif/',views.FifthPageView),
    path('sd/', views.showdateView)
]