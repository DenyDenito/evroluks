from django.conf.urls import url
from .views import BlogEntryList, BlogEntryDetail

urlpatterns = [
    url(r'^$', BlogEntryList.as_view(), name='blog_list'),
    url(r'^(?P<slug>[-\w]+)/$', BlogEntryDetail.as_view(), name='blog_detail'),
]
