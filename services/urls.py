from django.conf.urls import url
from .views import ServiceList, ServiceDetail

urlpatterns = [
    url(r'^$', ServiceList.as_view(), name='services'),
    url(r'^(?P<pk>[-\d]+)/$', ServiceDetail.as_view(), name='service_detail'),
]
