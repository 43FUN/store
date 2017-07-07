# -*- coding: utf-8 -*-
from django import template
from django.shortcuts import get_object_or_404

from store.forms import FeedbackForm
from store.models import Wallet

register = template.Library()


@register.assignment_tag()
def feedback_form():
    return FeedbackForm
