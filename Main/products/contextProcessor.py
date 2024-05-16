from products.models import Category_one,Category_two

def category(request):
    return {
        'categories':Category_one.objects.all(),
        'categories_two':Category_two.objects.all()
    }
