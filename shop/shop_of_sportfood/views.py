from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import NewProducts


def main(request):
    picture = Pictures.objects.all()
    contex = {
        'picture': picture,
    }
    return render(request, 'shop_of_sportfood/main.html', contex)


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
            try:
                Products.objects.create(**form.cleaned_data)
                return redirect('products')

            except:
                form.add_error(None, "Ошибка добавления поста")
    else:
        form = NewProducts()

    contex = {
        'form': form,
        # 'error': error
    }
    return render(request, 'shop_of_sportfood/zakaz.html', contex)


def register(request):
    return render(request, 'shop_of_sportfood/register.html')


def show_product(request, product_id):
    product = Products.objects.all()
    contex = {
        'product': product,
        'product_id': product_id,
    }
    return render(request, 'shop_of_sportfood/opred_product.html', contex)


def show_category(request, cat_id):
    title = Category.objects.all()
    product = Products.objects.filter(cat_id=cat_id)
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
