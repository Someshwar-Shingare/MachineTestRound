from django.shortcuts import render
# Create your views here.
def homeView(request):
    template_name = 'FirstApp/home.html'
    context = {}
    return render(request,template_name,context)
def aboutView(request):
    template_name = 'FirstApp/about.html'
    context = {}
    return render(request,template_name,context)
def loginView(request):
    template_name = 'FirstApp/login.html'
    context = {}
    return render(request,template_name,context)
def registerView(request):
    template_name = 'FirstApp/register.html'
    context = {}
    return render(request,template_name,context)
def contactView(request):
    template_name = 'FirstApp/contact.html'
    context = {}
    return render(request,template_name,context)
