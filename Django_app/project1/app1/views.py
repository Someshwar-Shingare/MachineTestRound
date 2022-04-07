from django.http import HttpResponse
def view1(request):
    return HttpResponse("Hello")
def view2(request):
    return HttpResponse("<h1>Bye</h1>")

# Create your views here.
