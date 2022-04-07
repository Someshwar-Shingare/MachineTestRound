from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Laptop

# Create your views here.
class HomeView(TemplateView):
    template_name = 'CBVCRUDapp/home.html'

class LaptopCreateView(CreateView):
    model = Laptop
    fields = '__all__'
    success_url = '/cbv/list/'
    #template_name = 'CBVCRUDapp/laptop_form.html'

class LaptopListView(ListView):
    model = Laptop
    # context_object_name = 'object_list'
    # template_name = 'CBVCRUDapp/laptop_list.html'

class LaptopUpdateView(UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = '/cbv/list/'

class LaptopDeleteView(DeleteView):
    model = Laptop
    success_url = '/cbv/list/'
    # template_name = 'CBVCRUDapp/laptop_confirm_delete.html'

