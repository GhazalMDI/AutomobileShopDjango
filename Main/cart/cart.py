CART_SESSION_ID = 'cart'
from products.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        if not self.session.get(CART_SESSION_ID):
            self.session[CART_SESSION_ID] = {}
        self.cart = self.session.get(CART_SESSION_ID)


    def AddToCart(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'slug': product.slug, 'name': product.name, 'quantity': 0,
                                     'unit_price': str(product.unit_price)}

        if self.cart[product_id]['quantity'] + quantity > product.stock:
            return False

        self.cart[product_id]['quantity'] += quantity
        self.save()
        return True

    def save(self):
        self.session.modified = True


    def RemoveOneCart(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            if self.cart[product_id]['quantity'] > 1:
                self.cart[product_id]['quantity'] -= 1
                self.save()
                return True
            del self.cart[product_id]
            self.save()
            return True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for p in products:
            cart[str(p.id)]['id'] = p.id
            cart[str(p.id)]['image'] = p.image.url
            # cart[str(p.id)]['unit_price'] = p.unit_price
            cart[str(p.id)]['after_discount'] = p.after_discount
            cart[str(p.id)]['discount'] = p.discount
            cart[str(p.id)]['url'] = p.get_absolute_url

        for item in cart.values():
            item['total'] = item['quantity'] * item['after_discount']
            yield item



    @property
    def get_total_price(self):
        return sum(
            i['quantity'] * int(i['unit_price']) for i in self.cart.values()
        )

    def __len__(self):
        return sum(1 for i in self.cart.values())

    def clear_all(self):
        self.session.get(CART_SESSION_ID).clear()


