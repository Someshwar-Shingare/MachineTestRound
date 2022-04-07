from django.http import HttpResponse
from django.shortcuts import render
def ht7view(request):
    return render(request, "App3/ht7.html")
def ht8view(request):
    return render(request, "App3/ht8.html")


# Create your views here.
