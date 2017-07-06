# -*- coding: utf-8 -*-
from django import template
from django.shortcuts import get_object_or_404

from store.forms import FeedbackForm
from store.models import Wallet

register = template.Library()


@register.assignment_tag()
def feedback_form():
    return FeedbackForm


@register.assignment_tag(takes_context=True)
def wallet(context):
    wallet = get_object_or_404(Wallet, user=context.get('request').user)
    return wallet
