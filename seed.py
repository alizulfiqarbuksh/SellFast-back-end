# seed.py
from sqlalchemy.orm import Session, sessionmaker
from config.environment import db_URI
from sqlalchemy import create_engine
from models.base import Base

# Import seed data
from data.user_data import user_list
from data.product_data import product_list
# from data.cart_data import cart_list, cart_item_list
from data.order_data import order_list, order_item_list

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")
    # Drop and recreate tables to ensure a clean slate
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("Seeding the database...")
    db = SessionLocal()

    # Seed users first
    print("  Adding users...")
    db.add_all(user_list)
    db.commit()

    # Seed products
    print("  Adding products...")
    db.add_all(product_list)
    db.commit()

    # # Seed carts
    # print("  Adding carts...")
    # db.add_all(cart_list)
    # db.commit()

    # # Seed cart items
    # print("  Adding cart items...")
    # db.add_all(cart_item_list)
    # db.commit()

    # Seed orders
    print("  Adding orders...")
    db.add_all(order_list)
    db.commit()

    # Seed order items
    print("  Adding order items...")
    db.add_all(order_item_list)
    db.commit()

    db.close()
    print("Database seeding complete! 🎉")

except Exception as e:
    print("An error occurred:", e)
