from django.shortcuts import render
def user1view(request):
    return render(request, "somesh.html")
def user2view(request):
    return render(request, "nagesh.html")
def user3view(request):
    return render(request, "ritesh.html")

class Student:
    def __init__(self,r,n,m):
        self.rn = r
        self.name = n
        self.marks = m
    def __str__(self):
        return f'Rn-{self.rn}, Name-{self.name}, Marks-{self.marks}'
s1=Student(1,'Sachin',80)
print(s1)

def userview(request):
   template_name = "user.html"
   context = {'name':'somesh','m':90,'age':'27years','condition':True,'li':[10,20,30,40,50],'obj':s1}
   return render(request,template_name,context)

# Create your views here.
