from django.http import HttpResponse
def view1(request):
    return HttpResponse("Hello from django")
def view2(request):
    return HttpResponse("Create New Project")
def view3(request):
    return HttpResponse("give the new name to project")
def view4(request):
    return HttpResponse("Create the New Python File")
def view5(request):
    return HttpResponse("Bye from Django")