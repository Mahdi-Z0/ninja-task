from ninja import Router
from myapp.models import order
from myapp.schemas import orderIn, orderOut
from typing import List
from django.shortcuts import get_object_or_404

order_router = Router()

@order_router.post('/add_order')
def post_order(request, data: orderIn):
    qs = order.objects.create(**data.dict())
    return {List[orderOut]}


@order_router.get('/', response={
    200:list[orderOut],
    404: None
})
def get(request):
    data = order.objects.all()
    
    if not data:
        return 404, None
    return 200, data

@order_router.delete("delete_order/{order_id}")
def delete_order(request, order_id: int):
    Order = get_object_or_404(order, id=order_id)
    Order.delete()
    return {"Deleted": True}
