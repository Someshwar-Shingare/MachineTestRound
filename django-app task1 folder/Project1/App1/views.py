from django.shortcuts import render
import datetime

# Create your views here.
def HomePageView(request):
    template_name = 'App1/home.html'
    context = {}
    return render(request,template_name,context)
def FirstPageView(request):
    template_name = 'App1/first.html'
    context = {'Emp1':[1,'Sachin','Engineer'],
               'Emp2':[2, 'Rahul','Doctor'],
               'Emp3':[3, 'Deepak', 'Teacher']}
    return render(request,template_name,context)
def SecondPageView(request):
    template_name = 'App1/second.html'
    context = {'St1':[1,'Pradeep','first'],
               'St2':[2, 'Avinash','second'],
               'St3':[3, 'Pralhad','third']}
    return render(request,template_name,context)
def ThirdPageView(request):
    template_name = 'App1/Third.html'
    context = {'Pro1':[1,'laptop',2],
               'Pro2':[2, 'tv',1],
               'Pro3':[3,'refrigerator',2]}
    return render(request,template_name,context)
def FourthPageView(request):
    template_name = 'App1/fourth.html'
    context = {'Tv1':['LG','2011','1yrs'],
               'Tv2':['Samsung', '2012','2yrs'],
               'Tv3':['Mi','2013','1yrs']}
    return render(request,template_name,context)
def FifthPageView(request):
    template_name = 'App1/fifth.html'
    context = {'Lap1':['HP','8gb',50000],
               'Lap2':['Asus','16gb',60000],
               'Lap3': ['Lenovo','32gb',70000]}
    return render(request,template_name,context)

def showdateView(request):
    datetime.datetime.now()
    return render(request,'index.html')


# Create your views here.
