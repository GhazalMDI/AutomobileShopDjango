# Generated by Django 5.0.2 on 2024-03-26 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_category_two_battery_alter_category_two_oil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_two',
            name='battery',
        ),
        migrations.RemoveField(
            model_name='category_two',
            name='oil',
        ),
    ]
