from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^about/$', views.about, name='about'),
    url(r'^clients/$', views.clients, name='clients'),
    url(r'^contacts/$', views.contacts, name='contacts'),
]
