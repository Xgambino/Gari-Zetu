from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .models import db
from flask_migrate import Migrate
# Import resources after initializing db to avoid circular import
from resources.catalogue import CatalogueResource 
from resources.add_catalogue import CatalogueAddResource

# from resources.news import NewsResource

# from config import Config  # Adjust the import path

app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dealership.db'
migrate = Migrate(app, db)
db.init_app(app)


api.add_resource(CatalogueResource, '/catalogues', '/catalogues/<int:catalogue_id>')
api.add_resource(CatalogueAddResource, '/add_catalogues', '/add_catalogues/<int:add_catalogue_id>')
# api.add_resource(NewsResource, '/news', '/news/<int:news_id>')

if __name__ == '__main__':
    app.run(debug=True)
