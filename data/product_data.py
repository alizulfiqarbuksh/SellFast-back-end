# data/product_data.py

from models.product import ProductModel

def create_products():
    products = [
        ProductModel(
            name="iPhone 15 Pro",
            description="Latest Apple smartphone with A17 Pro chip",
            price=999.99,
            stock=50,
            is_available=True,
            image = ""
        ),
        ProductModel(
            name="Samsung Galaxy S24",
            description="Flagship Android phone with AI features",
            price=849.99,
            stock=75,
            is_available=True,
            image = ""
        ),
        ProductModel(
            name="MacBook Pro 14",
            description="Powerful laptop with M3 Pro chip",
            price=1999.99,
            stock=30,
            is_available=True,
            image = ""
        ),
        ProductModel(
            name="Sony WH-1000XM5",
            description="Premium noise-cancelling headphones",
            price=349.99,
            stock=100,
            is_available=True,
            image = ""
        ),
        ProductModel(
            name="iPad Air",
            description="Versatile tablet with M1 chip",
            price=599.99,
            stock=60,
            is_available=True,
            image = ""
        ),
        ProductModel(
            name="Nintendo Switch OLED",
            description="Hybrid gaming console with OLED screen",
            price=349.99,
            stock=45,
            is_available=True,
            image = ""
        ),
        ProductModel(
            name="Apple Watch Series 9",
            description="Smartwatch with health tracking features",
            price=399.99,
            stock=80,
            is_available=True,
            image = ""
        ),
        ProductModel(
            name="Dell XPS 15",
            description="Premium Windows laptop with OLED display",
            price=1499.99,
            stock=25,
            is_available=True,
            image = ""
        ),
        ProductModel(
            name="AirPods Pro 2",
            description="Wireless earbuds with active noise cancellation",
            price=249.99,
            stock=120,
            is_available=True,
            image = ""
        ),
        ProductModel(
            name="PS5 Console",
            description="Sony PlayStation 5 gaming console",
            price=499.99,
            stock=20,
            is_available=True,
            image = ""
        ),
    ]
    return products

product_list = create_products()
