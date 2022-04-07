from django.shortcuts import render
def user1(request):
    return render(request, "App4/avinash.html")
def user2(request):
    return render(request, "App4/gajanan.html")
def user3(request):
    return render(request, "App4/pratik.html")


def empviews(request):
   template_name = "App4/users.html"
   context = {
              'Emp1':[1,'Sachin','Engineer','Nanded','Maharashtra',40000],
              'Emp2':[2, 'Rahul','Doctor','Hyderabad','Telangana',50000],
              'Emp3': [3, 'Deepak', 'Teacher', 'Patna',,'Bihar',30000],
              'Emp4':[4,'Pratik','Assistant','Banglore','Karnataka',25000],
              'Emp5':[5,'Avinash','Clerk','Panji','Goa',20000]}
   return render(request, template_name, context)



# Create your views here.
