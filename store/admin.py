# -*- coding: utf-8 -*-
from django.contrib import admin

from store.models import Products, ProductImage, Feedback, Wallet


class ProductsImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 0


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'novelty')
    inlines = [ProductsImageAdmin, ]

admin.site.register(Products, ProductsAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date')

admin.site.register(Feedback, FeedbackAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'money')

admin.site.register(Wallet, WalletAdmin)


