from models.review import ReviewModel

def create_reviews():
    return [
        ReviewModel(product_id=1, user_id=1, rating=5, comment="Perfect, exactly as described."),
        ReviewModel(product_id=1, user_id=2, rating=4.5, comment="Great phone, battery could be better."),
        ReviewModel(product_id=2, user_id=3, rating=4, comment="Solid Android experience."),
        ReviewModel(product_id=3, user_id=4, rating=5, comment="Amazing performance for dev work."),
        ReviewModel(product_id=4, user_id=5, rating=4.5, comment="Noise cancelling is top-tier."),
        ReviewModel(product_id=5, user_id=1, rating=4.5, comment="Great tablet, love the M1 chip."),
        ReviewModel(product_id=6, user_id=2, rating=5, comment="Best gaming console ever!"),
        ReviewModel(product_id=7, user_id=3, rating=4, comment="Good smartwatch, tracking is accurate."),
        ReviewModel(product_id=8, user_id=4, rating=4.5, comment="Beautiful OLED display."),
        ReviewModel(product_id=9, user_id=5, rating=5, comment="Sound quality is incredible."),
        ReviewModel(product_id=10, user_id=1, rating=4.5, comment="Worth every penny."),
    ]

review_list = create_reviews()