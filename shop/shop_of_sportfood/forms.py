from .models import Products
from django.forms import ModelForm , TextInput, Textarea,  FileInput, NumberInput, Select
# from django.forms import ModelForm


class NewProducts(ModelForm):
    class Meta:
        model = Products
        # fields = '__all__'
        fields = ['name', 'description', 'price', 'photo', 'author', 'cat']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название товара'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание товара'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену товара'
            }),
            "photo": FileInput(attrs={
                'class': 'form-control',
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите свое имя(никнейм)'
            }),
            "cat": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Введите категорию'
            })
         }
