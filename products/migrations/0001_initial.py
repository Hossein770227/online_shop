# Generated by Django 5.0.6 on 2024-06-16 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proudct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('short_description', models.CharField(max_length=200, verbose_name='short text')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('price_with_discount', models.PositiveIntegerField(verbose_name='price with discount')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('date_time_created', models.DateTimeField(auto_now_add=True, verbose_name='date time created')),
                ('date_time_modified', models.DateTimeField(auto_now=True, verbose_name='date time modified')),
            ],
        ),
    ]
