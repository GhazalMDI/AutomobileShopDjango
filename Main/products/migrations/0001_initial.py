# Generated by Django 5.0.2 on 2024-03-19 14:29

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandBattery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BrandOil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VolumeOil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('unit', models.CharField(choices=[('millilitre', 'میلی لیتر'), ('litre', 'لیتر')], default='litre', max_length=255)),
                ('number', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True)),
                ('Flow', models.PositiveIntegerField()),
                ('desc', models.TextField()),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='battery_brand', to='products.brandbattery')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Oil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True)),
                ('API', models.CharField(choices=[('SM', 'SM'), ('SN', 'SN'), ('SL', 'SL'), ('SF', 'SF')], default='SM', max_length=255)),
                ('Fuel_consumption', models.CharField(choices=[('Gasoline', 'گازوئیل'), ('oil', 'بنزین'), ('CNG', 'گازسوز')], default='oil', max_length=255)),
                ('Guarantee', models.CharField(choices=[('0W-30', '0W-30'), ('5W-30', '5W-30'), ('10W-30', '10W-30'), ('10W-40', '10W-40'), ('15W-40', '15W-40')], default='10W-30', max_length=255)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oil_brand', to='products.brandoil')),
                ('volume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oil_volume', to='products.volumeoil')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True)),
                ('unit_price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('battery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_battery', to='products.battery')),
                ('oil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_oil', to='products.oil')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]