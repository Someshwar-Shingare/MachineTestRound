from django.http import HttpResponse
def view1(request):
    return HttpResponse("Hello World!")