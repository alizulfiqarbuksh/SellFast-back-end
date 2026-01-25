from fastapi import APIRouter, Depends, HTTPException
# sqlalchemy
from sqlalchemy.orm import Session
from models.order import OrderModel
from models.user import UserModel
from models.order_item import OrderItemModel
from models.product import ProductModel
# serializers
from serializers.order import OrderSchema, OrderCreateSchema, OrderUpdateSchema
# database connection
from database import get_db
from typing import List
# middleware
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get("/orders", response_model=List[OrderSchema])
def get_all_orders(db: Session = Depends(get_db)):
    orders = db.query(OrderModel).all()
    return orders

@router.get("/orders/{order_id}", response_model=OrderSchema)
def get_one_order(order_id: int, db: Session = Depends(get_db)):
    
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if not order:
       raise HTTPException(status_code=404, detail="Order not found")

    return order

@router.post("/orders", response_model=OrderSchema)
def create_order(
    order: OrderCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized")

    new_order = OrderModel(
        user_id=current_user.id,
        total_price=0,
        status="pending"
    )

    total_price = 0

    for item in order.items:
        
        product = db.query(ProductModel).filter(ProductModel.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product with ID {item.product_id} not found")
        
        
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail=f"Quantity must be greater than zero for product {product.name}")
        
        if product.stock <= 0:
            raise HTTPException(status_code=400, detail=f"Product {product.name} is out of stock!")

        
        order_item = OrderItemModel(
            product_id=product.id,
            product_name=product.name,
            price=product.price,
            quantity=item.quantity
        )
        new_order.items.append(order_item)
        total_price += product.price * item.quantity
        product.stock -= item.quantity

    new_order.total_price = round(total_price, 2)

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@router.delete("/orders/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    found_order = db.query(OrderModel).filter(OrderModel.id == order_id).first()

    if not found_order:
        raise HTTPException(status_code=404, detail="Order not found")

    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized")

    db.delete(found_order)
    db.commit()
    return {"message": f"Order with ID {order_id} was deleted!"}