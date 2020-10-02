from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate,logout
from .models import Contacts,Products,Orders,OrderUpdate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import CreateUserLoginForm,CreateUserRegisterForm
# Create your views here.


def login_view(request):       
    form=CreateUserLoginForm()
    if request.method=='POST':
        form=CreateUserLoginForm(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')        
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/shop')
        else:
            messages.info(request,'Username OR Password is Incorrect')            
    return render(request,'shop/login.html',{'form':form})

def register_view(request):
    form=CreateUserRegisterForm()
    if request.method=='POST':
        print("$$!!WORKING!!$$")
        form=CreateUserRegisterForm(request.POST)
        if form.is_valid():
            print("$$!!VALID!!$$")
            form.save()
            messages.success(request,'Account was created Sucessfully')
            return redirect('/shop/login')
            # login(request,)
        else:
            print(form.errors); 
            
    return render(request,'shop/signup.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('/shop')

@login_required(login_url='/shop/login')
def index(request):
    prod=Products.objects.all()
    return render(request,"shop/index.html",{'prod':prod})

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    
    return render(request,'shop/contact.html')

def checkout(request):
    ok=0;
    if request.method=="POST":
        json=request.POST.get('json','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','') + ' '+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zipcode=request.POST.get('zipcode','')
        phone=request.POST.get('phone','')
        order=Orders(json=json,name=name,email=email,address=address,state=state,city=city,zipcode=zipcode,phone=phone)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="The Order has been Placed ")
        update.save()
        ok=1
    return render(request,'shop/checkout.html',{'ok':ok})

def tracker(request):
    return render(request,'shop/tracker.html')

def cart(request):
    products=Products.objects.all()
    return render(request,'shop/cart.html',{'products':products})

def productview(request,id):
    prod=Products.objects.filter(id=id)
    product=prod.first()
    return render(request,'shop/prodview.html',{'product':product})

def search(request):
    return render(request,'shop/search.html')
