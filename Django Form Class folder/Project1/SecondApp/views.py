
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm,RegisterForm,ContactForm

# Create your views here.
def loginView(request):
    if request.method == 'GET':
        template_name = 'SecondApp/login.html'
        form = LoginForm()
        context = {'form':form}
        return render(request,template_name,context)
    elif request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')

        return HttpResponse(f"{u},{p}")


def registerView(request):
    if request.method == 'GET':
        template_name = 'SecondApp/register.html'
        form = RegisterForm()
        context = {'form':form}
        return render(request,template_name,context)
    elif request.method == 'POST':
        n = request.POST.get('name')
        d = request.POST.get('dob')
        a = request.POST.get('age')
        c = request.POST.get('city')


        return HttpResponse(f"{n},{d},{a},{c}")



def contactView(request):
    if request.method == 'GET':
        template_name = 'SecondApp/contact.html'
        form = ContactForm()
        context = {'form':form}
        return render(request,template_name,context)
    elif request.method == 'POST':
        c = request.POST.get('contactno')
        e = request.POST.get('email')

        return HttpResponse(f"{c},{e}")


