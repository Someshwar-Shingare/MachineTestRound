from django.http import HttpResponse
def view1(request):
    return HttpResponse("hi")
def view2(request):
    return HttpResponse("Good Evening")
def view3(request):
    return HttpResponse("What are you doing?")
def view4(request):
    return HttpResponse("Where are you?")
def view5(request):
    return HttpResponse("Bye!!")