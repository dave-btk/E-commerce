# Generated by Django 3.2.7 on 2021-10-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_products_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(default=1),
        ),
    ]
