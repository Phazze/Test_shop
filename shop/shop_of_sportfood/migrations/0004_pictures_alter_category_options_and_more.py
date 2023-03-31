# Generated by Django 4.1.7 on 2023-03-31 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_of_sportfood', '0003_alter_products_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Продукты', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.FileField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
