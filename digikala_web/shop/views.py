from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.
def hello_world(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products}

    return render(request , "index.html" , context)

