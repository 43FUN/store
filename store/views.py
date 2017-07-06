# -*- coding: utf-8 -*-t
from django.views import generic
from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm

from store.forms import FeedbackForm
from store.models import Products


class FeedbackView(generic.CreateView):
    http_method_names = ['post']
    form_class = FeedbackForm

    def form_valid(self, form):
        if form.instance.email:
            data = ['Имя: {}'.format(form.cleaned_data['name']),
                    'Телефон: {}'.format(form.cleaned_data['phone']),
                    'Сообщение: {}'.format(form.cleaned_data['text'])]
            message = ' '.join(data)
            user_email = form.cleaned_data['email']
            send_mail('Обратный звонок', message, 'from@example.com',
                      [user_email, 'boroda@gmail.com'], fail_silently=False)
        form.save()

        return JsonResponse({'response': 'success'})


class ProductsListView(generic.ListView):
    queryset = Products.objects.all()


class ProductsDetailView(generic.DetailView):
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(
            Products, id=self.kwargs.get('pk')
        )
        return context


class RegistrationUserView(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'store/registration.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

