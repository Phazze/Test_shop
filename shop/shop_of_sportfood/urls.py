from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="home"),
    path('products', views.products, name="products"),
    path('input', views.zakaz, name='dobavlen'),
    path('sign up', views.register, name='sign up'),
    path('tovar/<int:product_id>', views.show_product, name='tovar'),
    path('category/<int:cat_id>', views.show_category, name='category'),
    path('about', views.about_us, name='about'),
    path('map', views.map, name='map')
]
