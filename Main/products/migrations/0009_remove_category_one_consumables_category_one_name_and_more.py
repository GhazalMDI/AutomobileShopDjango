# Generated by Django 5.0.2 on 2024-03-21 11:34

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_category_one_product_categoryone_consumables_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_one',
            name='Consumables',
        ),
        migrations.AddField(
            model_name='category_one',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category_one',
            name='slug',
            field=models.SlugField(allow_unicode=True, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Category_two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('slug', models.SlugField(allow_unicode=True, null=True, unique=True)),
                ('battery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consumables_battery', to='products.battery')),
                ('catagoryOne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat_two', to='products.category_one')),
                ('oil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consumables_oil', to='products.oil')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='categoryTwo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categoryTwoProduct', to='products.category_two'),
        ),
        migrations.DeleteModel(
            name='Consumables',
        ),
    ]
