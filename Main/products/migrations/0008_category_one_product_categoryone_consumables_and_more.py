# Generated by Django 5.0.2 on 2024-03-21 11:24

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_battery_remove_product_oil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated', django_jalali.db.models.jDateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='categoryOne',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categoryOneProduct', to='products.category_one'),
        ),
        migrations.CreateModel(
            name='Consumables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consumables_battery', to='products.battery')),
                ('oil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consumables_oil', to='products.oil')),
            ],
        ),
        migrations.AddField(
            model_name='category_one',
            name='Consumables',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Consumables_categoryOne', to='products.consumables'),
        ),
    ]
