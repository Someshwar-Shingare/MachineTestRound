from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def loginView(request):
    if request.method == 'GET':
        print("GET req rcvd for loginView")
        template_name = 'App1/login.html'
        context = {}
        return render(request,template_name,context)
    elif request.method == 'POST':
        print("POST req rcvd for loginView")
        u = request.POST.get('username')
        p = request.POST.get('password')
        return HttpResponse(f"username={u},password={p}")


def registerView(request):
    if request.method == 'GET':
        print("GET req rcvd for registerView")
        template_name = 'App1/register.html'
        context = {}
        return render(request,template_name,context)
    elif request.method == 'POST':
        print("POST req rcvd for registerView")
        n = request.POST.get('name')
        d = request.POST.get('dob')
        a = request.POST.get('age')
        ad = request.POST.get('address')
        e =  request.POST.get('email')
        m =  request.POST.get('mobile number')
        g =  request.POST.get('gender')
        w =  request.POST.get('work experience')
        return HttpResponse(f"name={n},date of birth={d},age={a},address={ad},email={e},mobile number={m},gender={g},work experience={w}")
