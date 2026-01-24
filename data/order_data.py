# # data/order_data.py

# from models.order import OrderModel
# from models.order_item import OrderItemModel
# from datetime import datetime

# def create_orders():
#     orders = [
#         OrderModel(
#             user_id=1,
#             status="delivered",
#             total_price=1349.98,
#             created_at=datetime(2024, 1, 15, 10, 30)
#         ),
#         OrderModel(
#             user_id=2,
#             status="shipped",
#             total_price=2249.98,
#             created_at=datetime(2024, 1, 18, 14, 45)
#         ),
#         OrderModel(
#             user_id=3,
#             status="pending",
#             total_price=849.98,
#             created_at=datetime(2024, 1, 20, 9, 15)
#         ),
#         OrderModel(
#             user_id=4,
#             status="processing",
#             total_price=599.99,
#             created_at=datetime(2024, 1, 22, 16, 0)
#         ),
#     ]
#     return orders

# def create_order_items():
#     items = [
#         # Order 1 items (user 1)
#         OrderItemModel(order_id=1, product_id=1, product_name="iPhone 15 Pro", price=999.99, quantity=1),
#         OrderItemModel(order_id=1, product_id=4, product_name="Sony WH-1000XM5", price=349.99, quantity=1),
        
#         # Order 2 items (user 2)
#         OrderItemModel(order_id=2, product_id=3, product_name="MacBook Pro 14", price=1999.99, quantity=1),
#         OrderItemModel(order_id=2, product_id=9, product_name="AirPods Pro 2", price=249.99, quantity=1),
        
#         # Order 3 items (user 3)
#         OrderItemModel(order_id=3, product_id=2, product_name="Samsung Galaxy S24", price=849.99, quantity=1),
        
#         # Order 4 items (user 4)
#         OrderItemModel(order_id=4, product_id=5, product_name="iPad Air", price=599.99, quantity=1),
#     ]
#     return items

# order_list = create_orders()
# order_item_list = create_order_items()
