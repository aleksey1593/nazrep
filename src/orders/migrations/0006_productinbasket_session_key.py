# Generated by Django 3.0.4 on 2020-04-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_productinbasket'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
