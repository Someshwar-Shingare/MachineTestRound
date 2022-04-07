from django.urls import path
from .views import EmployerCreateView,EmployerListView,EmployerUpdateView,EmployerDeleteView
urlpatterns = [
    path('create/',EmployerCreateView.as_view(),name='emp_create'),
    path('home/',EmployerListView.as_view(),name='emp_list'),
    path('update/<int:pk>/',EmployerUpdateView.as_view(),name='emp_update'),
    path('delete/<int:pk>/',EmployerDeleteView.as_view(),name='emp_delete'),
]