# -*- coding: utf-8 -*-
from django import forms

from store.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'phone', 'email', 'text']
        model = Feedback
