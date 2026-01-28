from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.cart import CartModel
from models.user import UserModel
from serializers.cart import CartSchema, CartCreateSchema, CartUpdateSchema
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.post("/cart", response_model=CartSchema)
def create_cart(
    cart: CartCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    # Check if user already has a cart
    existing_cart = (
        db.query(CartModel)
        .filter(CartModel.user_id == current_user.id)
        .first()
    )

    if existing_cart:
        raise HTTPException(
            status_code=400,
            detail="User already has a cart",
        )

    new_cart = CartModel(
        user_id=current_user.id,
        is_active=cart.is_active,
    )

    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart


@router.put("/cart/{cart_id}", response_model=CartSchema)
def update_cart(
    cart_id: int,
    cart: CartUpdateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    found_cart = (
        db.query(CartModel)
        .filter(CartModel.id == cart_id)
        .first()
    )

    if not found_cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    # Ownership check
    if found_cart.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Unauthorized")

    cart_data = cart.model_dump(exclude_unset=True)
    for key, value in cart_data.items():
        setattr(found_cart, key, value)

    db.commit()
    db.refresh(found_cart)
    
    items = [
        {
            "id": item.id,
            "cart_id": item.cart_id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "product_name": item.product.name,
            "price": item.product.price,
        }
        for item in found_cart.items
    ]

    return {
        "id": found_cart.id,
        "user_id": found_cart.user_id,
        "is_active": found_cart.is_active,
        "items": items,
    }


@router.get("/cart/{cart_id}", response_model=CartSchema)
def get_one_cart(
    cart_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    cart = db.query(CartModel).filter(CartModel.id == cart_id).first()

    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    # same ownership check style as product admin check
    if cart.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Unauthorized")

    # Map cart items to include product_name and price
    items = [
        {
            "id": item.id,
            "cart_id": item.cart_id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "product_name": item.product.name,
            "price": item.product.price,
        }
        for item in cart.items
    ]

    return {
        "id": cart.id,
        "user_id": cart.user_id,
        "is_active": cart.is_active,
        "items": items,
    }