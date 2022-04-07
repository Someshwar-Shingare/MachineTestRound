
from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage




# Create your views here.
def contactView(request):
    template_name = 'DemoApp/contact.html'
    context = {}
    return render(request,template_name,context)

def showEmployeeView(request):
    employees = Employee.objects.all()
    paginator = Paginator(employees,2)
    page_number = request.GET.get('page')
    try:
        employees = paginator.page(page_number)
    except PageNotAnInteger:
        employees = paginator.page(2)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)
    return render(request, 'DemoApp/showemp.html', {'employees':employees})


def addEmployeeView(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'DemoApp/addemp.html'
    context = {'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def deleteEmployeeView(request,id):
    emp = Employee.objects.get(id=id)

    if request.method == 'POST':
        print(f"i = {id}")
        emp.delete()
        return redirect('home')
    template_name = 'DemoApp/deleteemp.html'
    context = {'emp': emp}
    return render(request, template_name, context)

@login_required(login_url='login')
def updateEmployeeView(request,id):
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(instance=emp)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=emp)
        if form. is_valid():
            form.save()
            return redirect('home')
    template_name = 'DemoApp/addemp.html'
    context = {'form': form}
    return render(request, template_name, context)


