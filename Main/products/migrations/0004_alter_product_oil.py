# Generated by Django 5.0.2 on 2024-03-19 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='oil',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='products.oil'),
        ),
    ]