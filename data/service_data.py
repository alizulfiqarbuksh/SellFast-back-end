from models.service import ServiceModel

def create_services():
    services = [
        ServiceModel(
            name="Laptop Repair",
            description="Expert repair for all laptop brands, including screen replacement and motherboard repair.",
            price=150.00,
            duration_minutes=120,
            is_available=True,
            image = ""
        ),
        ServiceModel(
            name="Mobile Screen Replacement",
            description="Fast and reliable screen replacement for iPhones and Android devices.",
            price=80.00,
            duration_minutes=60,
            is_available=True,
            image = ""
        ),
        ServiceModel(
            name="Software Installation",
            description="Installation of OS, productivity software, and custom applications.",
            price=50.00,
            duration_minutes=45,
            is_available=True,
            image = ""
        ),
        ServiceModel(
            name="Data Recovery",
            description="Professional data recovery from HDD, SSD, and USB drives.",
            price=200.00,
            duration_minutes=180,
            is_available=True,
            image = ""
        ),
        ServiceModel(
            name="Home Network Setup",
            description="Complete setup of Wi-Fi routers, extenders, and smart home devices.",
            price=120.00,
            duration_minutes=90,
            is_available=True,
            image = ""
        )
    ]
    return services

service_list = create_services()
