from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from products.models import Product
from cart.cart import Cart
from cart.forms import QuantityForm
class AddCartView(View):
    form_class = QuantityForm

    def get(self, request, slug, id):
        if product := get_object_or_404(Product, slug=slug, id=id):
            form = self.form_class(request.GET)
            if form.is_valid():
                quantity = form.cleaned_data['quantity']
                cart = Cart(request)
                res = cart.AddToCart(product=product, quantity=quantity)
                if res:
                    return redirect('accounts:Profile')
                return redirect('Home:home')
            cart = Cart(request)
            res = cart.AddToCart(product=product, quantity=1)
            if res:
                return redirect('accounts:Profile')
            return redirect('Home:home')


class RemoveOneToCart(View):
    def get(self, request, id, slug):
        if product := Product.objects.filter(id=id, slug=slug).first():
            cart = Cart(request)
            res = cart.RemoveOneCart(product)
            if res:
                return redirect('accounts:Profile')
            return redirect('products:products')

        return redirect('products:products')


class ClearCart(View):
    template_name = 'products/products.html'

    def get(self, request):
        cart = Cart(request)
        cart.clear_all()
        return render(request, self.template_name)
