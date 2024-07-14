from app import app, db  # Adjust import paths as necessary
from models import Catalogue, AddCatalogue, News  # Import your models

# Create instances of your models
catalogue1 = Catalogue(
    image_url='example_image_url',
    brand='example_brand',
    model='example_model',
    category='example_category',
    price='example_price',
    rating='example_rating',
    release_date='example_release_date'
)

# Wrap database operations in app context
with app.app_context():
    # Add instances to session and commit changes
    db.session.add(catalogue1)
    db.session.commit()

    print("Data seeded successfully!")
