from django.http import HttpResponse
from django.shortcuts import render
def ht4view(request):
    return render(request, "App2/ht4.html")
def ht5view(request):
    return render(request, "App2/ht5.html")
def ht6view(request):
    return render(request, "App2/ht6.html")



# Create your views here.
