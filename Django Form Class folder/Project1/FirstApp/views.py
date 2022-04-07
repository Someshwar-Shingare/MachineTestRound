from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def addstudentView(request):
    if request.method == 'GET':
        template_name = 'FirstApp/addstud.html'
        form = StudentForm()
        context = {'form':form}
        return render(request,template_name,context)
    elif request.method == 'POST':
        r = request.POST.get('rn')
        n = request.POST.get('name')
        m = request.POST.get('marks')
        return HttpResponse(f"{r},{n},{m}")

