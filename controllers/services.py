from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.service import ServiceModel
from models.user import UserModel
from serializers.service import ServiceSchema, ServiceCreateSchema, ServiceUpdateSchema
from database import get_db
from typing import List
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get("/services", response_model=List[ServiceSchema])
def get_all_services(db: Session = Depends(get_db)):
    
    services = db.query(ServiceModel).all()

    return services

@router.get("/services/{service_id}", response_model=ServiceSchema)
def get_one_service(service_id: int, db: Session = Depends(get_db)):
    
    service = db.query(ServiceModel).filter(ServiceModel.id == service_id).first()
    
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    
    return service

@router.post("/services", response_model=ServiceSchema)
def create_service(service: ServiceCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized - Admin access required")

    new_service = ServiceModel(**service.dict())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service

@router.put("/services/{service_id}", response_model=ServiceSchema)
def update_service(service: ServiceUpdateSchema, service_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    
    found_service = db.query(ServiceModel).filter(ServiceModel.id == service_id).first()

    if not found_service:
        raise HTTPException(status_code=404, detail="Service not found")
    
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized - Admin access required")
    
    service_data = service.dict(exclude_unset=True)
    for key, value in service_data.items():
        setattr(found_service, key, value)
    
    db.commit()
    db.refresh(found_service)
    return found_service

@router.delete("/services/{service_id}")
def delete_service(service_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    
    found_service = db.query(ServiceModel).filter(ServiceModel.id == service_id).first()

    if not found_service:
        raise HTTPException(status_code=404, detail="Service not found")
    
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized - Admin access required")
    
    db.delete(found_service)
    db.commit()
    return {"Message": f"Service with ID {service_id} was deleted!"}
