from django.urls import path
from .views import ContactView,EmployeeCreateView,EmployeeListView,EmployeeUpdateView,EmployeeDeleteView
urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('create/',EmployeeCreateView.as_view(),name='emp_create'),
    path('home/',EmployeeListView.as_view(),name='emp_list'),
    path('update/<int:pk>/',EmployeeUpdateView.as_view(),name='emp_update'),
    path('delete/<int:pk>/',EmployeeDeleteView.as_view(),name='emp_delete'),
]