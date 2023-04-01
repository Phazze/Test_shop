from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopHome.as_view(), name="home"),
    path('products', views.products, name="products"),
    path('input', views.AddProduct.as_view(), name='dobavlen'),
    # path('sign up', RegisterUser.as_view(), name='sign up'),
    path('tovar/<slug:product_slug>', views.ShowProduct.as_view(), name='tovar'),
    path('category/<slug:cat_slug>', views.ProductsCategory.as_view(), name='category'),
    path('about', views.about_us, name='about'),
    path('map', views.map, name='map'),
    path('pageNotFound', views.pageNotFound, name='error'),
]
