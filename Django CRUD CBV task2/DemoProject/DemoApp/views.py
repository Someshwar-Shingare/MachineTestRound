from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Employee



# Create your views here.

class ContactView(TemplateView):
    template_name = 'DemoApp/contact.html'


class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    success_url = '/dem/home/'
    #template_name = 'DemoApp/employee_form.html'

class EmployeeListView(ListView):
    model = Employee
    #context_object_name = 'object_list'
    #template_name = 'DemoApp/employee_list.html'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = '/dem/home/'

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/dem/home/'
    #template_name = 'DemoApp/employee_confirm_delete.html'


