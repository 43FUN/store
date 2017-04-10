# -*- coding: utf-8 -*-
from django.db import models
import datetime


class Feedback(models.Model):

    name = models.CharField('имя', max_length=50)
    email = models.EmailField('email', blank=True)
    phone = models.IntegerField('телефон')
    text = models.TextField('сообщение', max_length=500, blank=True)
    date = models.DateTimeField('дата', default=datetime.datetime.now)

    class Meta:
        verbose_name = 'обратный звонок'
        verbose_name_plural = 'обратные звонки'

    def __str__(self):
        return self.name


class Products(models.Model):

    title = models.CharField('название товара', max_length=100)
    description = models.TextField('описание товара', max_length=500)
    price = models.IntegerField('цена')
    quantity = models.IntegerField('количество товара')
    novelty = models.BooleanField('новинка?')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.title


class ProductImage(models.Model):

    product = models.ForeignKey(Products, related_name='product_image')
    product_image = models.ImageField('изображение товара', upload_to='product_image')

    class Meta:
        verbose_name = 'изображение товара'
        verbose_name_plural = 'изображения товаров'

    def __str__(self):
        return self.product_image.url
