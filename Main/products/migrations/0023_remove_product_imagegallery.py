# Generated by Django 5.0.2 on 2024-03-31 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_galleryproduct_product_imagegallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imageGallery',
        ),
    ]
