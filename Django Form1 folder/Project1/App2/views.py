from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login1View(request):
    if request.method == 'GET':
        print("GET req rcvd for login1View")
        template_name = 'App2/login1.html'
        context = {}
        return render(request, template_name, context)


    elif request.method == 'POST':
        print("POST req rcvd for login1View")
        u = request.POST.get('username')
        p = request.POST.get('password')
        return HttpResponse(f"username={u},password={p}")


def register1View(request):
    if request.method == 'GET':
        print("GET req rcvd for register1View")
        template_name = 'App2/register1.html'
        context = {}
        return render(request, template_name, context)
    elif request.method == 'POST':
        print("POST req rcvd for login1View")
        u = request.POST.get('username')
        p = request.POST.get('password')
        return HttpResponse(f"username={u},password={p}")




