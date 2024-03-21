from django.shortcuts import render
from product.models import product
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def about(request):
    return render(request,"about.html")

def home(request):
    username=request.session.get('currentUser',None)
    return render(request,"index.html",{"username" : username })


@login_required(login_url='/login/')
def search(request):
    query = request.GET.get('query','')
    print(query)
    productss=product.cm.query(query=query)
    print(productss)
    return render(request,"search.html",{'product':productss})


def Register(request):
    if request.method=="POST":
        #form=UserCreationForm(request.POST)
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        # form=UserCreationForm()
        form=RegisterForm()
    
    return render(request,'register.html',{"form":form})


def Login(request):
    if request.method=='POST':
        log_in=AuthenticationForm(request=request,data=request.POST)
        if log_in.is_valid():
            username=log_in.cleaned_data['username']
            password=log_in.cleaned_data['password']
            user=authenticate(username=username,password=password)
            
            if user is not None:
                login(request,user)
                request.session['currentUser']=user.get_username()
                return HttpResponseRedirect("/")
            
    else:
        log_in=AuthenticationForm(request.GET)
        #login=AuthenticationForm() #both are same
    return render(request,'login.html',{"login":log_in})




#User Logout Function

def Logout(request):
    logout(request)
    return HttpResponseRedirect("/login")