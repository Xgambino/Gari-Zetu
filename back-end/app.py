from flask import Flask
from flask_restful import Api,Resource
from models import db  # Assuming models.py is in the same directory
from flask_migrate import Migrate
from resources.catalogue import CatalogueResource
from resources.add_catalogue import CatalogueAddResource

app = Flask(__name__)
# app.config.from_object(Config)  # Uncomment and adjust as needed
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dealership.db'

# Initialize SQLAlchemy and Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)

# Initialize Flask-RESTful API
api = Api(app)

# Add RESTful resources to API
api.add_resource(CatalogueResource, '/catalogues', '/catalogues/<int:catalogue_id>')
api.add_resource(CatalogueAddResource, '/add_catalogues', '/add_catalogues/<int:add_catalogue_id>')
# Add other resources as needed

if __name__ == '__main__':
    app.run(debug=True)
