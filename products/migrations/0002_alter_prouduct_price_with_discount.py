# Generated by Django 5.0.6 on 2024-06-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prouduct',
            name='price_with_discount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='price with discount'),
        ),
    ]
