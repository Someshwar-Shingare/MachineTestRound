from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.testView,name='test'),
    path('show/',views.showLaptopsView,name='show'),
    path('add/',views.addLaptopView,name='add'),
    path('delete/<int:id>/',views.deleteLaptopView,name='delete'),
    path('update/<int:id>/',views.updateLaptopView,name='update'),

]