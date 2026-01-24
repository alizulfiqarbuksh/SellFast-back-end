from fastapi import APIRouter, Depends, HTTPException
# sqlalchemy
from sqlalchemy.orm import Session
from models.product import ProductModel
from models.user import UserModel
# serializers
from serializers.product import ProductSchema, ProductCreateSchema, ProductUpdateSchema
# databse connection
from database import get_db
from typing import List
# middleware
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get("/Products", response_model=List[ProductSchema])
def get_all_products(db: Session = Depends(get_db)):
  
  products = db.query(ProductModel).all()
  return products

@router.get("/Products/{product_id}", response_model=ProductSchema)
def get_one_product(product_id: int, db: Session = Depends(get_db)):

  product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
  
  if not product:
    raise HTTPException(status_code=404, detail="Product not found")
  
  return product

@router.post("/products", response_model=ProductSchema)
def create_product(product: ProductCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):

  if not current_user.is_admin:
    raise HTTPException(status_code=403, detail="Unauthorized")

  new_product = ProductModel(**product.dict())
  db.add(new_product)
  db.commit()
  db.refresh(new_product)
  return new_product

@router.put("/products/{product_id}", response_model=ProductSchema)
def update_product(product: ProductUpdateSchema, product_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):

  found_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

  if not found_product:
    raise HTTPException(status_code=404, detail="Product not found")
  
  if not current_user.is_admin:
    raise HTTPException(status_code=403, detail="Unauthorized")
  
  product_data = product.dict(exclude_unset=True)
  for key, value in product_data.items():
    setattr(found_product, key, value)
  
  db.commit()
  db.refresh(found_product)
  return found_product

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
  
  found_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

  if not found_product:
    raise HTTPException(status_code=404, detail="Product not found")
  
  if not current_user.is_admin:
    raise HTTPException(status_code=403, detail="Unauthorized")
  
  db.delete(found_product)
  db.commit()
  return {"Message": f"Product with ID {product_id} was deleted!"}