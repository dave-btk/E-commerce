# Generated by Django 3.2.7 on 2021-10-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_checkoutaddress_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutaddress',
            name='save_address',
            field=models.BooleanField(default=False),
        ),
    ]
