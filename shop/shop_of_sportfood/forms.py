from .models import Products, Category
from django import forms


# from django.forms import ModelForm


class NewProducts(forms.Form):
    name = forms.CharField(max_length=200, label="Название")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Описание')
    photo = forms.FileField(label="Фотография")
    price = forms.FloatField(label="Цена")
    author = forms.CharField(max_length=200, label="Автор")
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория")
    # class Meta:
    # model = Products
    # # fields = '__all__'
    # fields = ['name', 'description', 'price', 'photo', 'author', 'cat']
    # widgets = {
    #    "name": forms.CharField(attrs={
    #        'class': 'form-control',
    #        'placeholder': 'Введите название товара'
    #    }),
    #    "description": forms.TextField(attrs={
    #        'class': 'form-control',
    #        'placeholder': 'Введите описание товара'
    #    }),
    #    "price": forms.FloatField(attrs={
    #        'class': 'form-control',
    #        'placeholder': 'Введите цену товара'
    #    }),
    #    "photo": forms.FileField(attrs={
    #        'class': 'form-control',
    #    }),
    #    "author": forms.CharField(attrs={
    #        'class': 'form-control',
    #        'placeholder': 'Введите свое имя(никнейм)'
    #    }),
    #    "cat": forms.Select(attrs={
    #        'class': 'form-control',
    #        'placeholder': 'Введите категорию'
    #    })
    # }
