from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from models.cart_item import CartItemModel
from models.cart import CartModel
from models.product import ProductModel
from models.user import UserModel

from serializers.cart import CartItemCreateSchema, CartItemUpdateSchema, CartItemSchema
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

# ---------------------------
# GET all items in a cart
# ---------------------------
@router.get("/cart-items/{cart_id}", response_model=List[CartItemSchema])
def get_cart_items(cart_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):

    cart = db.query(CartModel).filter(CartModel.id == cart_id, CartModel.user_id == current_user.id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    
    # Mapping herre to return product name
    result = []
    for item in cart.items:
        result.append({
            "id": item.id,
            "cart_id": item.cart_id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "product_name": item.product.name,  # including the product name
            "price": item.product.price
        })
    return result

# ---------------------------
# CREATE a cart item
# ---------------------------
@router.post("/cart-items/{cart_id}", response_model=CartItemSchema)
def create_cart_item(cart_id: int, cart_item: CartItemCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):

    cart = db.query(CartModel).filter(CartModel.id == cart_id, CartModel.user_id == current_user.id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    
    product = db.query(ProductModel).filter(ProductModel.id == cart_item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    new_item = CartItemModel(cart_id=cart.id, product_id=cart_item.product_id, quantity=cart_item.quantity)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# ---------------------------
# UPDATE a cart item
# ---------------------------
@router.put("/cart-items/{item_id}", response_model=CartItemSchema)
def update_cart_item(item_id: int, cart_item: CartItemUpdateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):

    item = db.query(CartItemModel).join(CartModel).filter(
        CartItemModel.id == item_id, CartModel.user_id == current_user.id
    ).first()

    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    item.quantity = cart_item.quantity
    db.commit()
    db.refresh(item)
    return item

# ---------------------------
# DELETE a cart item
# ---------------------------
@router.delete("/cart-items/{item_id}")
def delete_cart_item(item_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):

    item = db.query(CartItemModel).join(CartModel).filter(
        CartItemModel.id == item_id, CartModel.user_id == current_user.id
    ).first()

    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    db.delete(item)
    db.commit()
    return {"Message": f"Cart item with ID {item_id} was deleted!"}
