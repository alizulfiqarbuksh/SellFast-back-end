from typing import Optional
from pydantic import BaseModel

class UserRegistrationSchema(BaseModel):
    username: str  # User's unique name
    email: str  # User's email address
    password: str  # Plain text password for user registration (will be hashed before saving)
    is_admin: bool = False

# New schema for user login (captures username and password during login)
class UserLoginSchema(BaseModel):
    username: str  # Username provided by the user during login
    password: str  # Plain text password provided by the user during login

    # New schema for the response (containing the JWT token and a success message)
class UserTokenSchema(BaseModel):
    token: str  # JWT token generated upon successful login
    message: str  # Success message
    cart_id: Optional[int] = None

    class Config:
      orm_mode = True

# Schema for returning user data (without exposing the password)
class UserSchema(BaseModel):
  username: str
  email: str

  class Config:
    orm_mode = True

