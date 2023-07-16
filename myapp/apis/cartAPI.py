from ninja import Router
from myapp.models import cart
from myapp.schemas import cartSchema
from typing import List
from django.shortcuts import get_object_or_404



cart_router = Router()

@cart_router.post('/add_cart')
def post_cart(request, data: cartSchema):
    qs = cart.objects.create(**data.dict())
    return {List[cartSchema]}

@cart_router.get('/display_cart', response={
    200:List[cartSchema],
    404: None
    })
def get_cart(request):
    data = cart.objects.all()
    
    if not data:
        return 404, None
    return 200, data

@cart_router.delete("delete_cart/{cart_id}")
def delete_cart(request, cart_id: int):
    Cart = get_object_or_404(cart, id=cart_id)
    Cart.delete()
    return {"Deleted": True}