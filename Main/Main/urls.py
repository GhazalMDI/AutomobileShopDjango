from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = ([
                   path('admin/', admin.site.urls),
                   path('', include('home.urls', namespace='Home')),
                   path('accounts/', include('accounts.urls', namespace='accounts')),
                   path('products/', include('products.urls', namespace='products')),
                   path('cart/', include('cart.urls', namespace='cart')),
               ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
