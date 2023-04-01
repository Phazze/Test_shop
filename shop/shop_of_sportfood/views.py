from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic import CreateView, ListView

from .models import *
from .forms import NewProducts


class ShopHome(ListView):
    model = Pictures
    template_name = 'shop_of_sportfood/main.html'
    context_object_name = 'picture'


# def main(request):
#     picture = Pictures.objects.all()
#     contex = {
#         'picture': picture,
#     }
#     return render(request, 'shop_of_sportfood/main.html', contex)


def products(request):
    title = Category.objects.all()
    product = Products.objects.order_by('-id')
    contex = {
        'category': title,
        'product': product,
        'cat_selected': 0
    }
    return render(request, 'shop_of_sportfood/products.html', contex)


def zakaz(request):
    # error = ''
    if request.method == "POST":
        form = NewProducts(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('products')
    else:
        form = NewProducts()

    contex = {
        'form': form,
        # 'error': error
    }
    return render(request, 'shop_of_sportfood/zakaz.html', contex)


def register(request):
    return render(request, 'shop_of_sportfood/register.html')


# class DataMixin:
#     pass


# class RegisterUser(DataMixin, CreateView):


def show_product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    contex = {
        'product': product,
        'product_id': product_slug,
    }
    return render(request, 'shop_of_sportfood/opred_product.html', contex)


def show_category(request, cat_id):
    title = Category.objects.all()
    product = Products.objects.filter(cat_id=cat_id)

    if len(product) == 0:
        raise Http404()

    contex = {
        'category': title,
        'product': product,
        'cat_selected': 0
    }
    return render(request, 'shop_of_sportfood/products.html', contex)


def about_us(request):
    return render(request, 'shop_of_sportfood/about.html')


def map(request):
    return render(request, 'shop_of_sportfood/map.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Page not found.</h1>")
