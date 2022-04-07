from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentForm
from .models import Student

# Create your views here.
def addStudentFormView(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            r = form.cleaned_data['rn']
            n = form.cleaned_data['name']
            m = form.cleaned_data['marks']
            st = Student(rn=r,name=n,marks=m)
            st.save()
            return HttpResponse(f"{r},{n},{m} Data Inserted")
    template_name = 'FormsApp/addstud.html'
    form = StudentForm()
    context = {'form':form}
    return render(request,template_name,context)

