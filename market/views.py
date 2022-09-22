from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . models import Category, Product


# Create your views here.

def home(request):
    return render(request, 'index.html')


def market(request):
    category = Category.objects.all()
    return render(request, 'home.html',
                  {'category': category})


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html',
                  {'products': products})



def CategoryDetailView(request, cats):
    products_category = Product.objects.filter(category = cats)
    return render(request, 'category-details.html',
                  {'cats' :cats , 'products_category': products_category})

