# Generated by Django 5.0.2 on 2024-03-27 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_product_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='battery',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='category_two',
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
            model_name='category_two',
            name='oil',
        ),
        migrations.DeleteModel(
            name='BrandBattery',
        ),
        migrations.DeleteModel(
            name='Battery',
        ),
        migrations.DeleteModel(
            name='BrandOil',
        ),
        migrations.DeleteModel(
            name='VolumeOil',
        ),
        migrations.DeleteModel(
            name='Oil',
        ),
    ]