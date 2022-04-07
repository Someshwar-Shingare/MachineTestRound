from django.urls import path
from . import views
urlpatterns = [
    path('add-laptop/',views.addLaptopModelFormView,name='add'),
    path('show-laptop/',views.showAllLaptopsView,name='show')

]