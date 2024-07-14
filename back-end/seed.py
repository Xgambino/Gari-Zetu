from app import app, db  # Adjust import paths as necessary
from models import Catalogue, AddCatalogue, News  # Import your models

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

# # Create instances for news blog
# news1 = News(
#     title='New Model Release: Toyota Camry 2023',
#     content='Toyota has just released its latest model of the Camry for 2023, featuring new technological advancements and an updated design.',
#     author='John Doe',
#     publication_date='2023-01-15'
# )

# news2 = News(
#     title='Honda Civic 2023: A Comprehensive Review',
#     content='The 2023 Honda Civic has been reviewed by experts and it continues to impress with its performance and reliability.',
#     author='Jane Smith',
#     publication_date='2023-02-20'
# )

# news3 = News(
#     title='Ford Mustang 2023: Power and Style',
#     content='Ford Mustang’s latest 2023 model combines power and style, making it a top choice for sports car enthusiasts.',
#     author='Mike Johnson',
#     publication_date='2023-03-25'
# )

# news4 = News(
#     title='Chevrolet Tahoe 2023: The Ultimate Family SUV',
#     content='Chevrolet has released the 2023 Tahoe, an SUV that offers ample space, comfort, and advanced safety features for families.',
#     author='Emily White',
#     publication_date='2023-04-10'
# )

# news5 = News(
#     title='Tesla Model 3 2023: The Future of Electric Cars',
#     content='Tesla’s 2023 Model 3 continues to lead the way in the electric car market with its innovative features and impressive range.',
#     author='Alex Green',
#     publication_date='2023-05-05'
# )

# Wrap database operations in app context
with app.app_context():
    # Add instances to session and commit changes
    db.session.add(catalogue1)
    db.session.commit()

    print("Data seeded successfully!")
