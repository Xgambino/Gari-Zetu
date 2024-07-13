from app import db
from models import Catalogue, AddCatalogue, News

db.create_all()

# Add seed data for Catalogue
catalogue1 = Catalogue(
    image_url="https://example.com/image1.jpg",
    brand="Toyota",
    model="Camry",
    category="Sedan",
    price="30000",
    rating="4.5",
    release_date="2022-01-01"
)

catalogue2 = Catalogue(
    image_url="https://example.com/image2.jpg",
    brand="Honda",
    model="Civic",
    category="Sedan",
    price="25000",
    rating="4.3",
    release_date="2022-02-01"
)

db.session.add(catalogue1)
db.session.add(catalogue2)

# Add seed data for AddCatalogue
add_catalogue1 = AddCatalogue(
    image_url="https://example.com/image3.jpg",
    brand="Toyota",
    model="Corolla",
    category="Sedan",
    price="20000",
    rating="4.2",
    release_date="2022-03-01"
)

db.session.add(add_catalogue1)

# Add seed data for News
news1 = News(
    image_url="https://example.com/image4.jpg",
    description="New car models arriving this summer!",
    ticket_price="100",
    date="2022-04-01"
)

db.session.add(news1)

db.session.commit()
