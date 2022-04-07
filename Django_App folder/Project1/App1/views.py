from django.http import HttpResponse
from django.shortcuts import render
def loginview(request):
    return render(request, "App1/login.html")
def templateview(request):
    return render(request, "App1/template.html")
def ht1view(request):
    return render(request, "App1/ht1.html")
def ht2view(request):
    return render(request, "App1/ht2.html")
def ht3view(request):
    return render(request, "App1/ht3.html")

# Create your views here.
