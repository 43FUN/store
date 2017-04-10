# -*- coding: utf-8 -*-
from django import template
from store.forms import FeedbackForm
from store.models import Products

register = template.Library()


@register.assignment_tag()
def feedback_form():
    return FeedbackForm


@register.assignment_tag()
def products():
    products = Products.objects.all()
    return products

