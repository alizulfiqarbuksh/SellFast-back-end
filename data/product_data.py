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
            image = "https://images-cdn.ubuy.co.in/65344ddf3b9264736e23ca36-straight-talk-apple-iphone-15-pro.jpg"
        ),
        ProductModel(
            name="Samsung Galaxy S24",
            description="Flagship Android phone with AI features",
            price=849.99,
            stock=75,
            is_available=True,
            image = "https://microless.com/cdn/products/e5be629aaecac00535731b8ffefd65b9-hi.jpg"
        ),
        ProductModel(
            name="MacBook Pro 14",
            description="Powerful laptop with M3 Pro chip",
            price=1999.99,
            stock=30,
            is_available=True,
            image = "https://cdsassets.apple.com/live/SZLF0YNV/images/sp/111902_mbp14-silver2.png"
        ),
        ProductModel(
            name="Sony WH-1000XM5",
            description="Premium noise-cancelling headphones",
            price=349.99,
            stock=100,
            is_available=True,
            image = "https://www.ashrafsbahrain.com/media/catalog/product/cache/214388c7319d64ac6dc1f8b96ae4f150/w/h/wh-1000xm5b_1_.jpg"
        ),
        ProductModel(
            name="iPad Air",
            description="Versatile tablet with M1 chip",
            price=599.99,
            stock=60,
            is_available=True,
            image = "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/ipad-air-11-inch-m2.png"
        ),
        ProductModel(
            name="Nintendo Switch OLED",
            description="Hybrid gaming console with OLED screen",
            price=349.99,
            stock=45,
            is_available=True,
            image = "https://pimcdn.sharafdg.com/images/S100691391_1?1738236428"
        ),
        ProductModel(
            name="Apple Watch Series 9",
            description="Smartwatch with health tracking features",
            price=399.99,
            stock=80,
            is_available=True,
            image = "https://196bh.com/images/thumbs/100/100018058_750.jpeg"
        ),
        ProductModel(
            name="Dell XPS 15",
            description="Premium Windows laptop with OLED display",
            price=1499.99,
            stock=25,
            is_available=True,
            image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXaTKLN4dLtsmi8ZmHbX1KAxNfJEISlM-Y9A&s"
        ),
        ProductModel(
            name="AirPods Pro 2",
            description="Wireless earbuds with active noise cancellation",
            price=249.99,
            stock=120,
            is_available=True,
            image = "https://m.media-amazon.com/images/I/61sRKTAfrhL._AC_UF350,350_QL80_.jpg"
        ),
        ProductModel(
            name="PS5 Console",
            description="Sony PlayStation 5 gaming console",
            price=499.99,
            stock=20,
            is_available=True,
            image = "https://pimcdn.sharafdg.com/cdn-cgi/image/width=600,height=600,fit=pad,format=webp,quality=70/images/S500915267_1?1738236608"
        ),
        ProductModel(
            name="Asus ROG Strix Scar 15",
            description="A ROG PC Designed for esports and heavy multitasking, it offers up to a 300Hz FHD or 165Hz QHD display",
            price=1799.99,
            stock=10,
            is_available=True,
            image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBZ6w69W7o505LTRbBgq0mqpS6ALcRx8_s8A&s"
        ),
    ]
    return products

product_list = create_products()
