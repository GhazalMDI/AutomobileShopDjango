from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from products.models import *
from django.views import View
from django.core.paginator import Paginator
from urllib.parse import urlencode
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from products.filters import ProductFilter
from products.forms import CommentForm


class ProductsView(View):
    template_name = 'products/products.html'

    def get(self, request, slug=None, id=None):
        products = Product.objects.filter(available=True)
        search = request.GET.get('SearchBox')
        if search and id and slug:
            products = products.filter(name__contains=search)
        if id and slug:
            products = products.filter(
                Q(categoryOne__id=id, categoryOne__slug=slug) | Q(categoryTwo__id=id,  categoryTwo__slug=slug))
            cats = products.first()
            filters = ProductFilter(request.GET, products)
            products = filters.qs
            paginator = Paginator(products, 10)
            page = request.GET.get('page')
            products = paginator.get_page(page)
            url_data = request.GET.copy()
            if 'page' in url_data:
                del url_data['page']
            ctx = {
                'url_data': urlencode(url_data),
                'filters': filters,
                'products': products,
                'catname': cats,
            }
            return render(request, self.template_name, ctx)

        if search:
            products = products.filter(name__contains=search)
            filters = ProductFilter(request.GET, products)
            products = filters.qs
            cats = products.first()
            paginator = Paginator(products, 10)
            page = request.GET.get('page')
            products = paginator.get_page(page)
            url_data = request.GET.copy()
            if 'page' in url_data:
                del url_data['page']
            ctx = {
                'filters': filters,
                'products': products,
                'catname': cats,
                'url_data': urlencode(url_data)

            }
            return render(request, self.template_name, ctx)
        filters = ProductFilter(request.GET, products)
        products = filters.qs
        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        url_data = request.GET.copy()
        if 'page' in url_data:
            del url_data['page']
        ctx = {
            'filters': filters,
            'products': products,
            'url_data': urlencode(url_data),
        }
        return render(request, self.template_name, ctx)


class ProductDetailsView(View):
    template_name = 'products/ProductDetails.html'
    comment_Form = CommentForm
    def setup(self, request, *args, **kwargs):
        self.products = get_object_or_404(Product, id=kwargs['id'], slug=kwargs['slug'])
        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        product = self.products
        comments = Comment.objects.filter(product_id=product.id, active=True,is_replay=False)
        length = len(Comment.objects.filter(active=True,product_id=product.id))
        ctx = {
            'length': length,
            'comments': comments,
            'product': product,
            'form': CommentForm()
        }
        return render(request, self.template_name, ctx)
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        product = self.products
        form = self.comment_Form(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.product = product
            if comment_id := request.GET.get('cm_id'):
                replay_to = get_object_or_404(Comment,id=comment_id)
                com.replay_to = replay_to
                com.is_replay = True
            com.save()
            return redirect('products:productDetails', product.slug, product.id)
        ctx = {
            'product': product,
            'form': form
        }
        return render(request, self.template_name, ctx)
class LikeView(View):
    template_name = 'accounts/Profile.html'

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        if product:
            obj, created = Like.objects.get_or_create(product=product, user=request.user)
            if created:
                return redirect('accounts:Profile')
            obj.delete()
            return redirect('products:productDetails', product.slug, product.id)

        return redirect('products:products')


class RemoveLikeView(View):
    template_name = 'accounts/Profile.html'

    def get(self, request, slug):
        product = get_object_or_404(Like, product__slug=slug, user=request.user)
        if product:
            product.delete()
            return redirect('accounts:Profile')
        return redirect('products:products')
