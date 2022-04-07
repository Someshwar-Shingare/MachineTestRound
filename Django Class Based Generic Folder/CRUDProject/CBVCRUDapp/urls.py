from django.urls import path
from .views import HomeView,LaptopCreateView,LaptopListView,LaptopUpdateView,LaptopDeleteView
urlpatterns = [
    path('home/',HomeView.as_view(),name='home'),
    path('create/',LaptopCreateView.as_view(),name='lap_create'),
    path('list/',LaptopListView.as_view(),name='lap_list'),
    path('update/<int:pk>/',LaptopUpdateView.as_view(),name='lap_update'),
    path('delete/<int:pk>/',LaptopDeleteView.as_view(),name='lap_delete'),
]