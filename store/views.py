from django.views import generic
from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect

from store.forms import FeedbackForm
from store.models import Products, Wallet


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


class RegistrationUserView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'store/registration.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect('/')


class LoginUserView(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'store/login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)


class LogoutUserView(generic.View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class BuyProductView(generic.View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        product_id = self.request.POST.get('product_id', None)
        product = get_object_or_404(Products, id=product_id)
        wallet = get_object_or_404(Wallet, user=request.user)
        if wallet.money >= product.price:
            new_balance = wallet.money - product.price
            wallet.money = new_balance
            wallet.save()
            response = 'success'
        else:
            response = 'fail'

        return JsonResponse({'response': response})
