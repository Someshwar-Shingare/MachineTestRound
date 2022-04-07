
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def testView(request):
    return render(request,'AuthApp/test.html')
def registerView(request):
    form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('User Added')
            form.save()
            return redirect('login')
    template_name = 'AuthApp/register.html'
    context = {'form':form}
    return render(request,template_name,context)


def loginView(request):
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pw')

        user = authenticate(username=u,password=p)
        print(f'user={user}')

        if user is not None:
            print('Valid Credentials,Logging In....')
            login(request,user)
            return redirect('emp_list')
        else:
            print('Invalid Credentials,loading same login page again')
            messages.error(request,'Invalid Credentials,Please Try Again!')
    template_name = 'AuthApp/login.html'
    context = {}
    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login')

