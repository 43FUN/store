# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 09:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('phone', models.IntegerField(verbose_name='телефон')),
                ('text', models.TextField(blank=True, max_length=500, null=True, verbose_name='сообщение')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='дата')),
            ],
            options={
                'verbose_name': 'обратный звонок',
                'verbose_name_plural': 'обратные звонки',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(upload_to='product_image', verbose_name='изображение товара')),
            ],
            options={
                'verbose_name': 'изображение товара',
                'verbose_name_plural': 'изображения товаров',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название товара')),
                ('description', models.TextField(max_length=500, verbose_name='описание товара')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('quantity', models.IntegerField(verbose_name='количество товара')),
                ('novelty', models.BooleanField(verbose_name='новинка?')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='store.Products'),
        ),
    ]
