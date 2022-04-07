from django.shortcuts import render

class Employee:
    def __init__(self,i,n,d,c,st,sal):
        self.eid=i
        self.ename=n
        self.edesignation=d
        self.ecity=c
        self.estate=st
        self.esalary=sal
e1 = Employee(1,'Sachin','Engineer','Nanded','Maharashtra',40000)
e2 = Employee(2,'Rahul','Doctor','Hyderabad','Telangana',50000)
e3 = Employee(3,'Deepak','Teacher','Patna','Bihar',30000)
e4 = Employee(4,'Pratik','Assistant','Banglore','Karnataka',25000)
e5 = Employee(5,'Avinash','Clerk','Panji','Goa',20000)


def empviews(request):
   template_name = "App1/home.html"
   context = {'Emplist':[]}
   return render(request, template_name, context)


# Create your views here.
