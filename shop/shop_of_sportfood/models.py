from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.FileField(upload_to='photos/%Y/%m/%d/')
    price = models.FloatField()
    author = models.CharField(max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
    time_upload = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tovar', kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
