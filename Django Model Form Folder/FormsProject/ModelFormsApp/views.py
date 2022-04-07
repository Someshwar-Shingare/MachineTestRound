from django.shortcuts import render,redirect
from .forms import LaptopModelForm
from .models import Laptop

# Create your views here.
def addLaptopModelFormView(request):
    if request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'ModelFormsApp/addlaptop.html'
    form = LaptopModelForm()
    context = {'form':form}
    return render(request,template_name,context)

def showAllLaptopsView(request):
    template_name = 'ModelFormsApp/alllaps.html'
    laptops = Laptop.objects.all()
    context = {'laptops':laptops}
    return render(request,template_name,context)
