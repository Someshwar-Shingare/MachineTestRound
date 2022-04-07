from django.http import HttpResponse
def view5(request):
    return HttpResponse("This is view5 page")
def view6(request):
    return HttpResponse("<h1>This is view6 page</h1>")


# Create your views here.
