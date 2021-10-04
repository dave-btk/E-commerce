# Generated by Django 3.2.7 on 2021-10-04 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0013_alter_products_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='label',
            field=models.CharField(choices=[('N', 'New'), ('BS', 'Best Seller'), ('CL', 'Clearance'), ('EV', 'Ever Green')], max_length=2),
        ),
        migrations.CreateModel(
            name='ProductOrdered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('total_price', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
