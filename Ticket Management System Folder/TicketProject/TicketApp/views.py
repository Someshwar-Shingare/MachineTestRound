from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import TicketForm

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import TicketForm, CreateUserForm
from .filters import TicketFilter


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')

		context = {'form': form}
		return render(request, 'TicketApp/register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'TicketApp/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


def home(request):
	tickets = Ticket.objects.all()

	total_tickets = tickets.count()
	delivered = tickets.filter(status='Delivered').count()
	pending = tickets.filter(status='Pending').count()

	context = {'tickets':tickets,'total_tickets':total_tickets,'delivered':delivered,
	'pending':pending }

	return render(request, 'TicketApp/dashboard.html', context)




def createTicket(request):
	form = TicketForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = TicketForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'TicketApp/ticket_form.html', context)

def updateTicket(request, pk):

	ticket = Ticket.objects.get(id=pk)
	form = TicketForm(instance=ticket)

	if request.method == 'POST':
		form = TicketForm(request.POST, instance=ticket)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'TicketApp/ticket_form.html', context)

def deleteTicket(request, pk):
	ticket = Ticket.objects.get(id=pk)
	if request.method == "POST":
		ticket.delete()
		return redirect('/')

	context = {'item':ticket}
	return render(request, 'TicketApp/delete.html', context)