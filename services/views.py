from django.views.generic import ListView, DetailView
from .models import Service

# Create your views here.

class ServiceList(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'service_list'


class ServiceDetail(DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service_detail'
