from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt

# Import the secret from the environment file
from config.environment import secret

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserModel(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)

    # Relationships (use string names - SQLAlchemy resolves them at runtime)
    # cart = relationship("CartModel", back_populates="user", uselist=False, cascade="all, delete-orphan")
    # orders = relationship("OrderModel", back_populates="user")

    # Instance methods
    def set_password(self, password: str):
        self.password = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password)

    def generate_token(self):
        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(days=1),
            "iat": datetime.now(timezone.utc),
            "sub": str(self.id),
            "username": self.username,
            "is_admin": self.is_admin,
        }
        token = jwt.encode(payload, secret, algorithm="HS256")
        return token