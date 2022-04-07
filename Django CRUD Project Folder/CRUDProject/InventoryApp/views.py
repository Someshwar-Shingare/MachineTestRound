from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def testView(request):
    template_name = 'layout.html'
    context = {}
    return render(request,template_name,context)

def showProductView(request):
    template_name = 'InventoryApp/showprods.html'
    products = Product.objects.all()
    context = {'products':products}
    return render(request,template_name,context)

@login_required(login_url='login')
def addProductView(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'InventoryApp/addprod.html'
    context = {'form':form}
    return render(request,template_name,context)


@login_required(login_url='login')
def deleteProductView(request,id):
    prod = Product.objects.get(id=id)

    if request.method == 'POST':
        print(f"i = {id}")
        prod.delete()
        return redirect('show')
    template_name = 'InventoryApp/deleteprod.html'
    context = {'prod': prod}
    return render(request, template_name, context)

def updateProductView(request,id):
    prod = Product.objects.get(id=id)
    form = ProductForm(instance=prod)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=prod)
        if form. is_valid():
            form.save()
            return redirect('show')
    template_name = 'InventoryApp/addprod.html'
    context = {'form': form}
    return render(request, template_name, context)

