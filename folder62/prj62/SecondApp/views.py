from django.shortcuts import render
def loginView(request):
   template_name = "SecondApp/login.html"
   context = {}
   return render(request, template_name, context)
def registerView(request):
   template_name = "SecondApp/register.html"
   context = {}
   return render(request, template_name, context)




# Create your views here.
