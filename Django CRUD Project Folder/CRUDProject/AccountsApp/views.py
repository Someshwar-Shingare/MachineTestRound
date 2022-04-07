from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.views import View

# Create your views here.
def testView(request):
    return render(request,'AccountsApp/test.html')
def signupView(request):
    form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('User Added')
            form.save()
            return redirect('login')
    template_name = 'AccountsApp/signup.html'
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
            next = request.GET.get('next')
            print('next=',next)
            if next is None:
                return redirect('show')
            else:
                return redirect(next)
            return redirect('show')
        else:
            print('Invalid Credentials,loading same login page again')
            messages.error(request,'Invalid Credentials,Please Try Again!')
    template_name = 'AccountsApp/login.html'
    context = {}
    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login')

def testView(request):
    r = request.GET.get('rn')
    if r is not None:
        print('r is None',r)
    else:
        print('r got the value',r)
    return HttpResponse(f"testView got called,Query Param={r}")

def fbView(request):
    if request.method == 'POST':
        print('Fetch data fro frontend & process it further(save into DB)')
        un = request.POST.get('uname')
        return HttpResponse(f'save to DB-{un}')
    else:
        template_name = 'AccountsApp/temp.html'
        context = {}
        print('Render a template')
        return render(request,template_name,context)


class ClassBasedView(View):

    def get(self,request):
        template_name = 'AccountsApp/temp.html'
        context = {}
        print('Render a template')
        return render(request, template_name, context)

    def post(self,request):
        print('Fetch data frontend & process it further(save top DB)')
        un = request.POST.get('uname')
        return HttpResponse(f'save to DB-{un}')



