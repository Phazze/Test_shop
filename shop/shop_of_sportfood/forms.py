from .models import Products, Category
from django import forms


# from django.forms import ModelForm


class NewProducts(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Products
        # fields = '__all__'
        fields = ['name', 'slug', 'description', 'price', 'photo', 'author', 'cat']
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название товара'
            }),
            "slug": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название товара'
            }),
            "description": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание товара'
            }),
            "price": forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену товара'
            }),
            "author": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите свое имя(никнейм)'
            }),
            "cat": forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Введите категорию'
            })
        }
