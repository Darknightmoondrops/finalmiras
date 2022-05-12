from django.shortcuts import render
from Taksathi.models import Products
from .models import Sliders

def home_page(request):
    products = Products.objects.filter(status=True).all()[:8]
    sliders = Sliders.objects.all()
    context = {
        'products': products,
        'sliders': sliders,
    }
    return render(request,'Home/home_page/home_page.html', context)