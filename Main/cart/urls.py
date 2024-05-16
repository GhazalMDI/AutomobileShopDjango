from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('<slug>/<int:id>/',views.AddCartView.as_view(),name='cart'),
    path('removeOne/<int:id>/<slug>/',views.RemoveOneToCart.as_view(),name='RemoveOneCart'),
    path('clear/',views.ClearCart.as_view(),name='clearAll')

]