from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.testView,name='test'),
    path('show/',views.showProductView,name='show'),
    path('add/',views.addProductView,name='add'),
    path('delete/<int:id>/',views.deleteProductView,name='delete'),
    path('update/<int:id>/',views.updateProductView,name='update'),

]