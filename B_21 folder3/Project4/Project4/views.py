from django.http import HttpResponse
def view1(request):
    return HttpResponse("Python")
def view2(request):
    return HttpResponse("java")
def view3(request):
    return HttpResponse("C language")
def view4(request):
    return HttpResponse("C++ language")
def view5(request):
    return HttpResponse("Ruby")
