# data/cart_data.py

from models.cart import CartModel
from models.cart_item import CartItemModel

def create_carts_and_items():
    # Create carts for some users (user_id will be 1, 2, 3 after seeding)
    cart1 = CartModel(user_id=1, is_active=True)
    cart2 = CartModel(user_id=2, is_active=True)
    cart3 = CartModel(user_id=3, is_active=True)

    return [cart1, cart2, cart3]

def create_cart_items():
    # Cart items (cart_id and product_id reference seeded data)
    items = [
        CartItemModel(cart_id=1, product_id=1, quantity=1),  # iPhone for user 1
        CartItemModel(cart_id=1, product_id=4, quantity=2),  # Headphones for user 1
        CartItemModel(cart_id=2, product_id=3, quantity=1),  # MacBook for user 2
        CartItemModel(cart_id=2, product_id=9, quantity=1),  # AirPods for user 2
        CartItemModel(cart_id=3, product_id=6, quantity=1),  # Nintendo Switch for user 3
    ]
    return items

cart_list = create_carts_and_items()
cart_item_list = create_cart_items()
