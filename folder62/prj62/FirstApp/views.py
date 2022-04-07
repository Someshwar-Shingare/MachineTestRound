from django.shortcuts import render
def homeView(request):
   template_name = "FirstApp/home.html"
   context = {}
   return render(request, template_name, context)
def aboutView(request):
   template_name = "FirstApp/about.html"
   context = {}
   return render(request, template_name, context)



# Create your views here.
