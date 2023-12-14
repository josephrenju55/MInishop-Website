from django.urls import path
from . import views

urlpatterns = [
    path('cart',views.cart, name='cart'),
    path('add/<int:product_id>',views.add_cart, name='addcart'),
    path('cart_decrement/<int:product_id>/',views.min_cart, name='cart_decrement'),
    path('remove/<int:product_id>/', views.cart_delete, name='remove'),
    path('checkout',views.check_out, name='checkout'),
    path('payment',views.payments, name='payment'),
    path('pay',views.pay, name='pay'),

]