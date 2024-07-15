from app import app
from models import Catalogue, db, AddCatalogue, News  # Import your models

# Create instances of your models
catalogue1 = Catalogue(
    image_url='https://imgd.aeplcdn.com/664x374/n/cw/ec/110233/camry-exterior-right-front-three-quarter-3.jpeg?isig=0&q=80',
    brand='Toyota',
    model='Camry',
    category='Sedan',
    price='KES2,400,00',
    rating='4.5',
    release_date='2023-01-01'
)

catalogue2 = Catalogue(
    image_url='https://d2q68z18seh9hj.cloudfront.net/wp-content/uploads/2020/08/27182529/Civic-Sedan-LX-in-Platinum-Pearl-White.png',
    brand='Honda',
    model='Civic',
    category='Sedan',
    price='KES 3,200,000',
    rating='4.6',
    release_date='2023-02-01'
)

catalogue3 = Catalogue(
    image_url='https://hips.hearstapps.com/hmg-prod/images/2025-ford-mustang-60th-anniversary-exterior-66227932bb88e.jpg?crop=0.596xw:1.00xh;0.199xw,0&resize=768:*',
    brand='Ford',
    model='Mustang',
    category='Coupe',
    price='KES 3,600,000',
    rating='4.8',
    release_date='2023-03-01'
)

catalogue4 = Catalogue(
    image_url='https://www.chevrolet.com/content/dam/chevrolet/na/us/english/index/vehicles/2024/suvs/tahoe/trims/2023-tahoe-cc10706-1lz-g1w-trimselector.png?imwidth=960',
    brand='Chevrolet',
    model='Tahoe',
    category='SUV',
    price='KES 4,500,000',
    rating='4.7',
    release_date='2023-04-01'
)

catalogue5 = Catalogue(
    image_url='https://www.edmunds.com/assets/m/cs/blt993d3e8016b0c368/6568dd4adf42826a732f0d83/2025_model-3_f34_tesla_fe_9998_1122231_1280.jpg',
    brand='Tesla',
    model='Model 3',
    category='Sedan',
    price='KES 4,000,000',
    rating='4.9',
    release_date='2023-05-01'
)

# Create instances for news blog
news1 = News(
    image_url= 'https://i.ebayimg.com/images/g/b8wAAOSwE0JY~i3n/s-l1200.webp',
    description= 'New Model Release: Toyota Camry 2023',
    location= 'Mombasa,Kenya',
    ticket_price= 'KES 4,500', 
    date= '2024-08-15'
)
news2 = News(
    image_url= 'https://png.pngtree.com/png-clipart/20220429/original/pngtree-car-battery-charge-innovation-technology-vintage-poster-of-electric-vehicle-recharge-png-image_7569522.png',
    description= 'Electric Cars: The Future of Automotive Industry',
    location= 'Langata,Nairobi',
    ticket_price= 'KES 5,000', 
    date= '2024-09-11'
)
news3 = News(
    image_url= 'https://d1csarkz8obe9u.cloudfront.net/posterpreviews/car-rentals-poster-design-template-b6eec7913ae957e894b2b40d1643872b.jpg?ts=1637038220',
    description= 'How Self-Driving Cars Are Changing the World',
    location= 'Karen,Nairobi',
    ticket_price= 'KES 6,000', 
    date= '2024-12-31'
)
news4 = News(
    image_url= 'https://images.squarespace-cdn.com/content/v1/579ae8c9725e25911c587e32/5e2cd501-f45d-437f-9acd-f4be8a845f61/nathalia-cars-n-coffee-street-show.jpg?format=2500w',
    description= 'Cars and Coffee Nathalia',
    location= 'Nathalia, Victoria',
    ticket_price= 'Free Entry', 
    date= '2024-07-14'
)
news5 = News(
    image_url= 'https://images.squarespace-cdn.com/content/v1/579ae8c9725e25911c587e32/fb067e65-7747-46c2-b9d7-e861b1ed9530/violet-town-cares-and-coffee.jpg?format=2500w',
    description= 'Violet Town Cars & Coffee',
    location= 'Cowslip StreetViolet Town, VictoriaAustralia',
    ticket_price= 'Enquiries: Bill 0439420520 (txt)', 
    date= '2024-07-20'
)
news6 = News(
    image_url= 'https://cdn2.allevents.in/thumbs/thumb660a65cd79f5c.jpg',
    description= 'Scavenger Hunt at Karura',
    location= 'Karura Forest,Kenya',
    ticket_price= 'Enquiries: Bill 0439420520 (txt)', 
    date= '2024-08-21'
)
news7 = News(
    image_url= 'https://cdn-az.allevents.in/events9/banners/07fba9c7db645188ee520caf79c57d2a71708e42a1dfa9da81eb17a2859f2a3a-rimg-w1080-h1349-dcdc8c17-gmir?v=1720754435',
    description= 'TUNER FEST 4.0',
    location= 'Uhuru Gardens, Nairobi',
    ticket_price= 'Early Bird:KES 1,000', 
    date= '2024-08-18'
)
# Wrap database operations in app context
with app.app_context():
    Catalogue.query.delete()
    News.query.delete()
    # Add instances to session and commit changes
    db.session.add(catalogue1)
    db.session.add(catalogue2)
    db.session.add(catalogue3)
    db.session.add(catalogue4)
    db.session.add(catalogue5)

    db.session.add(news1)
    db.session.add(news2)
    db.session.add(news3)
    db.session.add(news4)
    db.session.add(news5)
    db.session.add(news6)
    db.session.add(news7)

    db.session.commit()

    print("Data seeded successfully!")
