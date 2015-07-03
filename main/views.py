from django.shortcuts import render
from promos.models import Promo
from services.models import Service
from .models import Slide


# Create your views here.

def main(request):
    promo_list = Promo.objects.all()
    service_list = Service.objects.all()
    slides = Slide.objects.all()
    return render(request, "index.html", {'promo_list': promo_list, 'service_list': service_list, 'slides': slides})


def about(request):
    return render(request, "about.html")


def clients(request):
    return render(request, "clients.html")


def contacts(request):
    return render(request, "contacts.html")
