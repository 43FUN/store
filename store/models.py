# -*- coding: utf-8 -*-
import datetime

from django.contrib.auth.models import User
from django.db import models


class Feedback(models.Model):

    name = models.CharField(
        verbose_name='имя',
        max_length=50
    )
    email = models.EmailField(
        verbose_name='email',
        blank=True
    )
    phone = models.IntegerField(
        verbose_name='телефон'
    )
    text = models.TextField(
        verbose_name='сообщение',
        max_length=500,
        blank=True)
    date = models.DateTimeField(
        verbose_name='дата',
        default=datetime.datetime.now
    )

    class Meta:
        verbose_name = 'обратный звонок'
        verbose_name_plural = 'обратные звонки'

    def __str__(self):
        return self.name


class Products(models.Model):

    title = models.CharField(
        verbose_name='название товара',
        max_length=100
    )
    description = models.TextField(
        verbose_name='описание товара',
        max_length=500
    )
    price = models.IntegerField(
        verbose_name='цена'
    )
    quantity = models.IntegerField(
        verbose_name='количество товара'
    )
    novelty = models.BooleanField(
        verbose_name='новинка?'
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.title


class ProductImage(models.Model):

    product = models.ForeignKey(
        to=Products,
        verbose_name='продукты',
        related_name='product_image')
    product_image = models.ImageField(
        verbose_name='изображение товара',
        upload_to='product_image'
    )

    class Meta:
        verbose_name = 'изображение товара'
        verbose_name_plural = 'изображения товаров'

    def __str__(self):
        return self.product_image.url


class Wallet(models.Model):

    user = models.OneToOneField(
        to=User,
        verbose_name='пользователь'
    )
    money = models.IntegerField(
        verbose_name='деньги',
        default=0
    )

    class Meta:
        verbose_name = 'кошелек'
        verbose_name_plural = 'кошельки'

    def __str__(self):
        return str(self.money)
