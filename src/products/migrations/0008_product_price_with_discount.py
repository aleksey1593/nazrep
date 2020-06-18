# Generated by Django 3.0.4 on 2020-04-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200405_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_with_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
