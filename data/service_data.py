from models.service import ServiceModel

def create_services():
    services = [
        ServiceModel(
            name="Laptop Repair",
            description="Expert repair for all laptop brands, including screen replacement and motherboard repair.",
            price=150.00,
            duration_minutes=120,
            is_available=True,
            image = "https://sakshicomputersudaipur.com/wp-content/uploads/2017/08/laptop_repairs.jpg"
        ),
        ServiceModel(
            name="Mobile Screen Replacement",
            description="Fast and reliable screen replacement for iPhones and Android devices.",
            price=80.00,
            duration_minutes=60,
            is_available=True,
            image = "https://img.freepik.com/premium-psd/smartphone-broken-screen-repair-service-social-media-post-design-template_47987-25261.jpg"
        ),
        ServiceModel(
            name="Software Installation",
            description="Installation of OS, productivity software, and custom applications.",
            price=50.00,
            duration_minutes=45,
            is_available=True,
            image = "https://5.imimg.com/data5/SELLER/Default/2025/8/537176259/SL/JI/UR/47063787/software-installation-services.png"
        ),
        ServiceModel(
            name="Data Recovery",
            description="Professional data recovery from HDD, SSD, and USB drives.",
            price=200.00,
            duration_minutes=180,
            is_available=True,
            image = "https://www.ensureservices.com/wp-content/uploads/2024/12/Blog6.jpg"
        ),
        ServiceModel(
            name="Home Network Setup",
            description="Complete setup of Wi-Fi routers, extenders, and smart home devices.",
            price=120.00,
            duration_minutes=90,
            is_available=True,
            image = "https://www.cablematters.com/blog/image.axd?picture=/HomeNetwork/How-to-set-up-a-home-network-a-complete-guide_1.jpg"
        )
    ]
    return services

service_list = create_services()
