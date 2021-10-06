# Generated by Django 3.2.7 on 2021-10-05 14:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_products_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=cloudinary.models.CloudinaryField(default=0, max_length=255, verbose_name='image'),
        ),
    ]