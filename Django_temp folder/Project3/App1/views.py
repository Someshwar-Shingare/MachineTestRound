from django.shortcuts import render
# Create your views here.
def homeView(request):
    template_name = 'App1/home.html'
    context = {}
    return render(request,template_name,context)
def aboutView(request):
    template_name = 'App1/about.html'
    context = {}
    return render(request,template_name,context)
def loginView(request):
    template_name = 'App1/login.html'
    context = {}
    return render(request,template_name,context)
def registerView(request):
    template_name = 'App1/register.html'
    context = {}
    return render(request,template_name,context)
def contactView(request):
    template_name = 'App1/contact.html'
    context = {}
    return render(request,template_name,context)
def baseView(request):
    template_name = 'App1/base.html'
    context = {}
    return render(request,template_name,context)
