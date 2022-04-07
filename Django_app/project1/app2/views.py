from django.http import HttpResponse
def view3(request):
    return HttpResponse("Hi,How are you?")
def view4(request):
    return HttpResponse("<h1>Where are you?</h1>")


# Create your views here.
