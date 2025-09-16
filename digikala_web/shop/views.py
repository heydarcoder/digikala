from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def hello_world(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products}

    return render(request , "index.html" , context)

def about(request):
    return render(request , 'about.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('hello_world')
        else:
            messages.success(request, 'شما وارد نشدید')
            return redirect('hello_world')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect("hello_world")
