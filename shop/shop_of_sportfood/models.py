from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Products(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание')
    photo = models.FileField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    price = models.FloatField(verbose_name='Цена')
    author = models.CharField(max_length=200, verbose_name='Автор')
    time_create = models.DateTimeField(auto_now_add=True)
    time_upload = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tovar', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'


class Pictures(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображения'
