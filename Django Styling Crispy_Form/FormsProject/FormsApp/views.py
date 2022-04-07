
from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def addStudentFormView(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():

            r = form.cleaned_data['rn']
            n = form.cleaned_data['name']
            m = form.cleaned_data['marks']
            st = Student(rn=r,name=n,marks=m)
            st.save()


            return redirect('show')
    template_name = 'FormsApp/addstud.html'

    context = {'form':form}
    return render(request,template_name,context)

def showAllStudentsView(request):
    template_name = 'FormsApp/showstuds.html'
    students = Student.objects.all()
    context = {'students': students}
    return render(request, template_name, context)




