from django.views.generic import ListView, DetailView
from .models import BlogEntry

# Create your views here.

class BlogEntryList(ListView):
    model = BlogEntry
    template_name = 'blog_list.html'
    context_object_name = 'blog_list'


class BlogEntryDetail(DetailView):
    template_name = 'blog_detail.html'
    model = BlogEntry
    context_object_name = 'blog_detail'
