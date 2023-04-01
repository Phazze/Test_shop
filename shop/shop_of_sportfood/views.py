from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import NewProducts


class ShopHome(ListView):
    model = Pictures
    template_name = 'shop_of_sportfood/main.html'
    context_object_name = 'picture'


def products(request):
    title = Category.objects.all()
    product = Products.objects.order_by('-id')
    contex = {
        'category': title,
        'product': product,
        'cat_selected': 0
    }
    return render(request, 'shop_of_sportfood/products.html', contex)


class AddProduct(LoginRequiredMixin, CreateView):
    form_class = NewProducts
    template_name = 'shop_of_sportfood/zakaz.html'
    login_url = reverse_lazy('home')
    raise_exception = True

def register(request):
    return render(request, 'shop_of_sportfood/register.html')


# class RegisterUser(DataMixin, CreateView):

class ShowProduct(DetailView):
    model = Products
    template_name = 'shop_of_sportfood/opred_product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'


class ProductsCategory(ListView):
    model = Products
    template_name = 'shop_of_sportfood/products.html'
    context_object_name = 'product'
    allow_empty = False

    def get_queryset(self):
        return Products.objects.filter(cat__slug=self.kwargs['cat_slug'])


def about_us(request):
    return render(request, 'shop_of_sportfood/about.html')


def map(request):
    return render(request, 'shop_of_sportfood/map.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Page not found.</h1>")
