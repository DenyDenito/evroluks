from django.conf.urls import url
from .views import PromoList, PromoDetail

urlpatterns = [
    url(r'^$', PromoList.as_view(), name='promos'),
    url(r'^(?P<pk>[-\d]+)/$', PromoDetail.as_view(), name='promo_detail'),
]
