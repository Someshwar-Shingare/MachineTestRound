from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contactView, name='contact'),
    path('',views.showEmployeeView,name='home'),
    path('add/',views.addEmployeeView,name='add'),
    path('delete/<int:id>/',views.deleteEmployeeView,name='delete'),
    path('update/<int:id>/',views.updateEmployeeView,name='update'),

]