# Generated by Django 5.0.2 on 2024-03-19 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_oil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='battery',
        ),
        migrations.RemoveField(
            model_name='oil',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='oil',
            name='volume',
        ),
        migrations.RemoveField(
            model_name='product',
            name='oil',
        ),
        migrations.AddField(
            model_name='product',
            name='API',
            field=models.CharField(blank=True, choices=[('SM', 'SM'), ('SN', 'SN'), ('SL', 'SL'), ('SF', 'SF')], default='SN', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Flow',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Fuel_consumption',
            field=models.CharField(blank=True, choices=[('Gasoline', 'گازوئیل'), ('oil', 'بنزین'), ('CNG', 'گازسوز')], default='oil', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Guarantee',
            field=models.CharField(blank=True, choices=[('0W-30', '0W-30'), ('5W-30', '5W-30'), ('10W-30', '10W-30'), ('10W-40', '10W-40'), ('15W-40', '15W-40')], default='10W-30', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='battery_brand', to='products.brandbattery'),
        ),
        migrations.AddField(
            model_name='product',
            name='brands',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oil_brand', to='products.brandoil'),
        ),
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('battery', 'Battery'), ('oil', 'Oil')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='volume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oil_volume', to='products.volumeoil'),
        ),
        migrations.DeleteModel(
            name='Battery',
        ),
        migrations.DeleteModel(
            name='Oil',
        ),
    ]
