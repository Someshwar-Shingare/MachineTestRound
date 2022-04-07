from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import SignupForm, AppointmentForm, AmbulanceForm, DoctorForm, NursingStaffForm, RoomServiceStaffForm, CategoryForm, ProductForm, FilterForm
from django.shortcuts import render,redirect
from .models import Appointment, Ambulance, Doctor, NursingStaff, RoomServiceStaff, Category, Product
from .filters import ProductFilter
from .cart import Cart
import razorpay
from django.views.decorators.csrf import csrf_exempt






# Create your views here.
def HomeView(request):
    template_name = 'healthify/home.html'
    context = {}
    return render(request,template_name,context)

def AdminView(request):
    template_name = 'healthify/admin.html'
    context = {}
    return render(request,template_name,context)

def CartView(request):
    template_name = 'healthify/cart.html'
    context = {}
    return render(request,template_name,context)



def storeView(request):
    products = None
    categories = Category.objects.all()
    categoryID = request.GET.get('category')

    if categoryID:
        products = Product.objects.filter(category=categoryID)
    else:
        products = Product.objects.all()

    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    context = {'products': products, 'categories': categories, 'myFilter': myFilter}
    return render(request, 'healthify/store.html', context)

def signupView(request):
    form = SignupForm()
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print('User Added')
            form.save()
            template = render_to_string('healthify/email_temp.html',{'name':request.POST.get('first_name')})
            mail = request.POST.get('email')
            name = request.POST.get('first_name')
            email = EmailMessage('Registration notification',template,settings.EMAIL_HOST_USER,[mail],)
            email.fall_silently = False
            email.send()
            return redirect('login')
    template_name = 'healthify/signup.html'
    context = {'form':form}
    return render(request,template_name,context)


def loginView(request):
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pw')

        user = authenticate(username=u,password=p)
        print(f'user={user}')

        if user is not None:
            print('Valid Credentials,Logging In....')
            login(request,user)
            return redirect('home')
        else:
            print('Invalid Credentials,loading same login page again')
            messages.error(request,'Invalid Credentials,Please Try Again!')
    template_name = 'healthify/login.html'
    context = {}
    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login')


# Create your views here.
def showAppointmentView(request):
    template_name = 'healthify/appointment_req.html'
    appointments = Appointment.objects.all()
    context = {'appointments':appointments}
    return render(request,template_name,context)


def addAppointmentView(request):

    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showapp')
    template_name = 'healthify/appointment.html'
    context = {'form':form}
    return render(request,template_name,context)




def deleteAppointmentView(request,id):
    appoint = Appointment.objects.get(id=id)

    if request.method == 'POST':
        print(f"i = {id}")
        appoint.delete()
        return redirect('showapp')
    template_name = 'healthify/delete_appointment.html'
    context = {'appoint': appoint}
    return render(request, template_name, context)


def showAmbulanceView(request):
    template_name = 'healthify/ambulance_req.html'
    ambulances = Ambulance.objects.all()
    context = {'ambulances':ambulances}
    return render(request,template_name,context)


def addAmbulanceView(request):
    form = AmbulanceForm()
    if request.method == 'POST':
        form = AmbulanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showamb')
    template_name = 'healthify/ambulance.html'
    context = {'form':form}
    return render(request,template_name,context)



def deleteAmbulanceView(request,id):
    pat = Ambulance.objects.get(id=id)

    if request.method == 'POST':
        print(f"i = {id}")
        pat.delete()
        return redirect('showamb')
    template_name = 'healthify/delete_ambulance.html'
    context = {'pat': pat}
    return render(request, template_name, context)




def showDoctorView(request):
    template_name = 'healthify/show_doctor.html'
    doctors = Doctor.objects.all()
    context = {'doctors':doctors}
    return render(request,template_name,context)


def addDoctorView(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showdoct')
    template_name = 'healthify/add_doctor.html'
    context = {'form':form}
    return render(request,template_name,context)



def deleteDoctorView(request,id):
    doct = Doctor.objects.get(id=id)

    if request.method == 'POST':
        print(f"i = {id}")
        doct.delete()
        return redirect('showdoct')
    template_name = 'healthify/delete_doctor.html'
    context = {'doct': doct}
    return render(request, template_name, context)

def updateDoctorView(request,id):
    doct = Doctor.objects.get(id=id)
    form = DoctorForm(instance=doct)
    if request.method == 'POST':
        form = DoctorForm(request.POST,instance=doct)
        if form. is_valid():
            form.save()
            return redirect('showdoct')
    template_name = 'healthify/add_doctor.html'
    context = {'form': form}
    return render(request, template_name, context)





def showNursingStaffView(request):
    template_name = 'healthify/show_nurse_staff.html'
    nursingstaffs = NursingStaff.objects.all()
    context = {'nursingstaffs':nursingstaffs}
    return render(request,template_name,context)


def addNursingStaffView(request):
    form =NursingStaffForm()
    if request.method == 'POST':
        form = NursingStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shownur')
    template_name = 'healthify/add_nurse_staff.html'
    context = {'form':form}
    return render(request,template_name,context)



def deleteNursingStaffView(request,id):
    nurse = NursingStaff.objects.get(id=id)

    if request.method == 'POST':
        print(f"i = {id}")
        nurse.delete()
        return redirect('shownur')
    template_name = 'healthify/delete_nurse_staff.html'
    context = {'nurse': nurse}
    return render(request, template_name, context)

def updateNursingStaffView(request,id):
    nurse = NursingStaff.objects.get(id=id)
    form = NursingStaffForm(instance=nurse)
    if request.method == 'POST':
        form = NursingStaffForm(request.POST,instance=nurse)
        if form. is_valid():
            form.save()
            return redirect('shownur')
    template_name = 'healthify/add_nurse_staff.html'
    context = {'form': form}
    return render(request, template_name, context)





def showRoomServiceStaffView(request):
    template_name = 'healthify/show_room_staff.html'
    roomservicestaffs = RoomServiceStaff.objects.all()
    context = {'roomservicestaffs':roomservicestaffs}
    return render(request,template_name,context)


def addRoomServiceStaffView(request):
    form = RoomServiceStaffForm()
    if request.method == 'POST':
        form = RoomServiceStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showrm')
    template_name = 'healthify/add_room_staff.html'
    context = {'form':form}
    return render(request,template_name,context)



def deleteRoomServiceStaffView(request,id):
    room = RoomServiceStaff.objects.get(id=id)

    if request.method == 'POST':
        print(f"i = {id}")
        room.delete()
        return redirect('showrm')
    template_name = 'healthify/delete_room_staff.html'
    context = {'room': room}
    return render(request, template_name, context)

def updateRoomServiceStaffView(request,id):
    room = RoomServiceStaff.objects.get(id=id)
    form = RoomServiceStaffForm(instance=room)
    if request.method == 'POST':
        form = RoomServiceStaffForm(request.POST,instance=room)
        if form. is_valid():
            form.save()
            return redirect('showrm')
    template_name = 'healthify/add_room_staff.html'
    context = {'form': form}
    return render(request, template_name, context)


def showCategoryView(request):
    template_name = 'healthify/show_category.html'
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,template_name,context)


def addCategoryView(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showcr')
    template_name = 'healthify/add_category.html'
    context = {'form':form}
    return render(request,template_name,context)



def deleteCategoryView(request,id):
    cat = Category.objects.get(id=id)

    if request.method == 'POST':
        print(f"i = {id}")
        cat.delete()
        return redirect('showcr')
    template_name = 'healthify/delete_category.html'
    context = {'cat': cat}
    return render(request, template_name, context)


def showProductView(request):
    category = request.GET.get('category')

    if category == None:
        products = Product.objects.order_by('price').filter(id=1)
    else:
        products = Product.objects.filter(name=category)
    template_name = 'healthify/show_product.html'
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products':products, 'categories':categories}
    return render(request,template_name,context)


def addProductView(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showpr')
    template_name = 'healthify/add_product.html'
    context = {'form':form}
    return render(request,template_name,context)



def deleteProductView(request,id):
    prod = Product.objects.get(id=id)

    if request.method == 'POST':
        print(f"i = {id}")
        prod.delete()
        return redirect('showpr')
    template_name = 'healthify/delete_product.html'
    context = {'prod': prod}
    return render(request, template_name, context)

def updateProductView(request,id):
    prod = Product.objects.get(id=id)
    form = ProductForm(instance=prod)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=prod)
        if form. is_valid():
            form.save()
            return redirect('showpr')
    template_name = 'healthify/add_product.html'
    context = {'form': form}
    return render(request, template_name, context)



def cart_display(request):
    cart =Cart(request)
    carts =cart.list()
    print(carts)
    return render(request,'healthify/cart.html')



def add_to_cart(request,id):
    if request.method == 'POST':
        print(request.session.get('product_cart'))
        product = Product.objects.get(id=id)
        quantity = request.POST['quantity']
        if not quantity:
            quantity = 1
        cart = Cart(request)
        cart.add(product,quantity)
        return redirect('/')



def customer_order(request):
	return render(request,'healthify/orders.html')



'''
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_9nmrK825fjo0Ym", "1f1icPZDRCKvac3lzpOmLSl1"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'store.html')

@csrf_exempt
def success(request):
    return render(request, "success.html")
'''




def index(request):
    context = {
        'products': Product.objects.all(),
        'form': FilterForm()
    }

    return render(request, 'healthify/index.html', context)
