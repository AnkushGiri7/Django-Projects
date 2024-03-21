from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.

def home(request):
    return HttpResponse('This is Home Page')

def about(request):
    return HttpResponse('This is About Page')

def firstPage(request):
    return HttpResponse('<h1>First Page</h1>')

def contactPage(request):
    return HttpResponse('This is Contact Page')

def users(request):
    school={
        'teacher':'It trainer',
        'students':55
    }
    return render(request,'index.html',school)

def loginuser(request):
    student={
        'id':101,
        'Name':'Nikita',
        'age':18
    }
    return render(request,'base.html',student)


def register_user(request):
    return render(request,"register.html")

def submit(request):
    if request.method == 'POST':
        return render(request,"submit.html")
    if request.method == 'GET':
        return render(request,"register.html")
    
class first_view(View):
    def get(self,request):
        return HttpResponse("Class Based View - GET")
    
    
class second_view(View):
    name = "Nisha"
    def get(self,request):
        return render(request,"second.html",{"name" : self.name})