# Generated by Django 3.2.7 on 2021-10-05 14:34

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='user_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
