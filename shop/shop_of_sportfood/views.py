from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import NewProducts, RegisterUserForm, LoginUserForm


class ShopHome(ListView):
    model = Pictures
    template_name = 'shop_of_sportfood/main.html'
    context_object_name = 'picture'


def products(request):
    title = Category.objects.all()
    product = Products.objects.order_by('-id')
    paginator = Paginator(product, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contex = {
        'category': title,
        'product': product,
        'page_obj': page_obj,
        'cat_selected': 0
    }
    return render(request, 'shop_of_sportfood/products.html', contex)


class AddProduct(LoginRequiredMixin, CreateView):
    form_class = NewProducts
    template_name = 'shop_of_sportfood/zakaz.html'
    login_url = reverse_lazy('home')
    raise_exception = True


# def register(request):
#     return render(request, 'shop_of_sportfood/register.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'shop_of_sportfood/register.html'
    success_url = reverse_lazy('sign in')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ShowProduct(DetailView):
    model = Products
    template_name = 'shop_of_sportfood/opred_product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'


class ProductsCategory(ListView):
    model = Products
    template_name = 'shop_of_sportfood/products.html'
    context_object_name = 'page_obj'
    allow_empty = False

    def get_queryset(self):
        return Products.objects.filter(cat__slug=self.kwargs['cat_slug'])


def about_us(request):
    return render(request, 'shop_of_sportfood/about.html')


def map(request):
    return render(request, 'shop_of_sportfood/map.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Page not found.</h1>")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'shop_of_sportfood/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('sign in')
