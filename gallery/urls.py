from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.gallery, name='gallery'),
    url(r'^(?P<pk>[-\d]+)/$', views.gallery, name='gallery'),
]
