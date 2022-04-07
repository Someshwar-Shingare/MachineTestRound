from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Employer

# Create your views here.
class EmployerCreateView(CreateView):
    model = Employer
    fields = '__all__'
    success_url = '/ca/home/'
    # template_name 'CRUDAuthApp/employer_form.html'

class EmployerListView(ListView):
    model = Employer
    # context_object_name = 'object_list'
    # template_name = 'CRUDAuthApp/employer_list.html'

class EmployerUpdateView(UpdateView):
    model = Employer
    fields = '__all__'
    success_url = '/ca/home/'

class EmployerDeleteView(DeleteView):
    model = Employer
    success_url = '/ca/home/'
    # template_name = 'CRUDAuthApp/employer_confirm_delete.html'

