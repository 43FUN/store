from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

from store.views import (
    FeedbackView, ProductsDetailView, ProductsListView, RegistrationUserView,
    LogoutUserView, LoginUserView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='store/index.html'), name='index'),
    url(r'^contacts/$', TemplateView.as_view(template_name='store/contacts.html'), name='contacts'),
    url(r'^products-list/$', ProductsListView.as_view(), name='products-list'),
    url(r'^products-list/products-detail-(?P<pk>\d+)/$', ProductsDetailView.as_view(), name='products-detail'),
    url(r'^contacts/feedback/$', FeedbackView.as_view(), name='feedback'),
    url(r'^registration$', RegistrationUserView.as_view(), name='registration'),
    url(r'^login$', LoginUserView.as_view(), name='login'),
    url(r'^logout$', LogoutUserView.as_view(), name='logout'),
]

urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
