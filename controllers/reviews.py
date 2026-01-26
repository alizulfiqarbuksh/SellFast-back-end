from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from typing import List

#models 
from models.review import ReviewModel
from models.product import ProductModel
from models.user import UserModel

#serializers
from serializers.review import ReviewSchema, CreateReviewSchema, UpdateReviewSchema, ReviewStatsSchema


#db
from database import get_db


#middleware 
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.post("/products/{product_id}/reviews", response_model=ReviewSchema)
def create_review(
    product_id: int, 
    review: CreateReviewSchema, 
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)):
    
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Check for duplicate review
    existing_review = db.query(ReviewModel).filter(
        ReviewModel.product_id == product_id,
        ReviewModel.user_id == current_user.id
    ).first()
    
    if existing_review:
        raise HTTPException(status_code=400, detail="You already reviewed this product")
    
    # Create new review
    new_review = ReviewModel(
        rating=review.rating,
        comment=review.comment,
        product_id=product_id, 
        user_id=current_user.id
    )
    
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    
    return new_review

@router.get("/products/{product_id}/reviews", response_model=List[ReviewSchema])
def get_reviews_of_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
         raise HTTPException(status_code=404, detail="product not found")
    return product.reviews

@router.get("/products/{product_id}/reviews", response_model=List[ReviewSchema])
def get_reviews_of_product(product_id: int, db: Session = Depends(get_db)):
    """Get all reviews for a specific product"""
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product.reviews


@router.get("/products/{product_id}/reviews/stats", response_model=ReviewStatsSchema)
def get_product_review_stats(product_id: int, db: Session = Depends(get_db)):
    
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    reviews = db.query(ReviewModel).filter(ReviewModel.product_id == product_id).all()
    
    if not reviews:
        return ReviewStatsSchema(
            product_id=product_id,
            total_reviews=0,
            average_rating=0.0,
            rating_distribution={1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        )
    
    total = len(reviews)
    avg_rating = sum(r.rating for r in reviews) / total
    
    # Calculate distribution
    distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for review in reviews:
        star = int(review.rating)  
        distribution[star] += 1
    
    return ReviewStatsSchema(
        product_id=product_id,
        total_reviews=total,
        average_rating=round(avg_rating, 2),
        rating_distribution=distribution
    )



@router.get("/reviews/{review_id}", response_model=ReviewSchema)
def get_review(review_id: int, db: Session = Depends(get_db)):
     review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
     if not review:
         raise HTTPException(status_code=404, detail="review not found")
     return review



@router.put("/reviews/{review_id}", response_model=ReviewSchema)
def update_review(
    review_id: int,
    review_data: UpdateReviewSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)):
   
    review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    
    # Check ownership
    if review.user_id != current_user.id:
        raise HTTPException(status_code=403,detail="You can only update your own reviews"
)
    
    # Update fields (only update provided fields)
    if review_data.rating is not None:
        review.rating = review_data.rating
    if review_data.comment is not None:
        review.comment = review_data.comment
    
    db.commit()
    db.refresh(review)
    
    return review


@router.delete("/reviews/{review_id}")
def delete_review(
    review_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)):
    
    review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    
    # Check ownership
    if review.user_id != current_user.id:
        raise HTTPException( status_code=403, detail="You can only delete your own reviews")
    
    db.delete(review)
    db.commit()
    
    return{"message":f"Review with ID {review_id} has been deleted"}