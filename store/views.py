# -*- coding: utf-8 -*-t
from django.views import generic
from django.http import JsonResponse
from django.core.mail import send_mail
from store.forms import FeedbackForm


class FeedbackView(generic.CreateView):
    http_method_names = ['post']
    form_class = FeedbackForm

    def form_valid(self, form):
        data = ['Имя: {}'.format(form.cleaned_data['name']),
                'Телефон: {}'.format(form.cleaned_data['phone']),
                'Сообщение: {}'.format(form.cleaned_data['text'])]
        message = ' '.join(data)
        user_email = form.cleaned_data['email']
        send_mail('Обратный звонок', message, 'from@example.com',
                  [user_email, 'boroda@gmail.com'], fail_silently=False)
        form = form.save(commit=False)
        form.save()

        return JsonResponse({'response': 'success'})
