# Generated by Django 5.0.2 on 2024-03-31 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_remove_product_imagegallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryproduct',
            name='imageGallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='galleryProduct', to='products.product'),
        ),
    ]
