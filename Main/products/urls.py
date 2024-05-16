from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('products/',views.ProductsView.as_view(),name='products'),
    path('products/<slug>/<int:id>/', views.ProductsView.as_view(), name='cat_products'),
    path('products/productDetails/<slug>/<int:id>/', views.ProductDetailsView.as_view(), name='productDetails'),
    path('products/AddLike/<slug>/',views.LikeView.as_view(),name='productsLike'),
    path('products/like/remove/<slug>/',views.RemoveLikeView.as_view(),name='removeProductsLike'),


    # path('products/searchBrand/',views.SearchBrandView.as_view(),name='searchBrand')
]