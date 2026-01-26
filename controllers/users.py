
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.cart import CartModel
from models.user import UserModel
from serializers.user import UserSchema, UserRegistrationSchema, UserLoginSchema, UserTokenSchema
from database import get_db

router = APIRouter()

@router.post("/register", response_model=UserTokenSchema)
def create_user(user: UserRegistrationSchema, db: Session = Depends(get_db)):
    # Check if the username or email already exists
    existing_user = db.query(UserModel).filter(
        (UserModel.username == user.username) | (UserModel.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(status_code=409, detail="Username or email already exists")

    new_user = UserModel(username=user.username, email=user.email, is_admin =user.is_admin)
    # Use the set_password method to hash the password
    new_user.set_password(user.password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Creating a cart for the user
    new_cart = CartModel(user_id=new_user.id)
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)

    token = new_user.generate_token()

    # Return token and a success message
    return {"token": token, "cart_id": new_cart.id, "message": "Registration successfull"}

@router.post("/login", response_model=UserTokenSchema)
def login(user: UserLoginSchema, db: Session = Depends(get_db)):

    # Find the user by username
    db_user = db.query(UserModel).filter(UserModel.username == user.username).first()

    # Check if the user exists and if the password is correct
    if not db_user or not db_user.verify_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Generate JWT token
    token = db_user.generate_token()

    user_cart = db.query(CartModel).filter(CartModel.user_id == db_user.id).first()
    cart_id = user_cart.id if user_cart else None

    # Return token and a success message
    return {"token": token, "cart_id": cart_id, "message": "Login successful"}