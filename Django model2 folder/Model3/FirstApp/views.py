from django.shortcuts import render
from .models import Student

# Create your views here.
def showStudents(request):
    template_name = 'FirstApp/showstuds.html'
    allStudents = Student.objects.all()
    context = {'allStudents': allStudents}
    return render (request,template_name,context)
