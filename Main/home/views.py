from django.shortcuts import render
from django.views import View

from home.models import Banner
from products.models import Product


class Home(View):
    template_name = 'home/home.html'

    def get(self, request):
        products = Product.objects.all()
        ctx = {
            'banners': Banner.objects.all(),
            'special':products.filter(discount__gt=1),
            'brakepads':products.filter(categoryTwo__slug='لنت-ترمز'),
            'airfilter':products.filter(categoryTwo__slug='فیلتر-هوا'),
            'oil': products.filter(categoryTwo__slug='روغن-موتور'),
            'battery': products.filter(categoryTwo__slug='باطری'),
        }
        return render(request, self.template_name, ctx)
