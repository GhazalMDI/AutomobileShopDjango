from cart.cart import Cart


def context_cart(request):
    return {
        'len_cart': Cart(request).__len__(),
    }
