# Generated by Django 5.0.2 on 2024-03-27 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_category_two_atrss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_two',
            name='atrss',
        ),
        migrations.AddField(
            model_name='category_two',
            name='atrss',
            field=models.ManyToManyField(related_name='attrs_cat_2', to='products.attributevalue'),
        ),
    ]
