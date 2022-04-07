from django.urls import path
from . import views
urlpatterns = [
    path('add-student/',views.addStudentFormView,name='add'),
    path('show-student/',views.showAllStudentsView,name='show')

]