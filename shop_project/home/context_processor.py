from . views import *
from home.views import *
from cart.views import *


def cate(request):
    cat=categ.objects.all()
    return {'data1':cat}

def cart_no(request):
    user=request.user
    tot=0
    count=0
    if user.is_authenticated:
        ct = cartlist.objects.filter(user=user)

    else:
        cart_id = request.session.get('cart_id')
        ct = cartlist.objects.filter(cart_id=cart_id)

    ct_items = cartitems.objects.filter(cart__in=ct, available=True)
    for i in ct_items:
        tot += (i.product.price * i.quantity)
        count += i.quantity
    return {"total_price":tot,"cn":count}