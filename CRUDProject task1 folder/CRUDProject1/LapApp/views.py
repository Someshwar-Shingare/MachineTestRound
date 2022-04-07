
from django.shortcuts import render,redirect
from .forms import LaptopForm
from .models import Laptop

# Create your views here.
def testView(request):
    template_name = 'base.html'
    context ={}
    return render(request,template_name,context)

def addLaptopView(request):
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'LapApp/addlaptop.html'
    context = {'form':form}
    return render(request,template_name,context)

def showLaptopsView(request):
    template_name = 'LapApp/showlaptops.html'
    laptops = Laptop.objects.all()
    context = {'laptops':laptops}
    return render(request,template_name,context)

def deleteLaptopView(request,id):
    print(f"i = {id}")
    lap = Laptop.objects.get(id=id)
    lap.delete()
    return redirect('show')

def updateLaptopView(request,id):
    lap = Laptop.objects.get(id=id)
    form = LaptopForm(instance=lap)
    if request.method == 'POST':
        form = LaptopForm(request.POST,instance=lap)
        if form. is_valid():
            form.save()
            return redirect('show')
    template_name = 'LapApp/addlaptop.html'
    context = {'form': form}
    return render(request, template_name, context)


