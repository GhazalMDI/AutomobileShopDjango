# Generated by Django 5.0.2 on 2024-04-11 07:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_replay',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='replay_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_replay', to='products.comment'),
        ),
    ]
