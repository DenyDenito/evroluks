from django.views.generic import ListView, DetailView
from .models import Promo

# Create your views here.

class PromoList(ListView):
    model = Promo
    template_name = 'promo_list.html'
    context_object_name = 'promo_list'


class PromoDetail(DetailView):
    model = Promo
    template_name = 'promo_detail.html'
    context_object_name = 'promo_detail'
