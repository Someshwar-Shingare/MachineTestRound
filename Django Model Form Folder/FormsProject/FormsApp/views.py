
from django.shortcuts import render,redirect
from .forms import StudentModelForm
from .models import Student

# Create your views here.
def addStudentModelFormView(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'FormsApp/addstud.html'
    form = StudentModelForm()
    context = {'form':form}
    return render(request,template_name,context)

def showAllStudentsView(request):
    template_name = 'FormsApp/allstud.html'
    students = Student.objects.all()
    context = {'students':students}
    return render(request,template_name,context)

