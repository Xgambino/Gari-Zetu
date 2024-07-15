from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy_serializer import SerializerMixin

# Create convention for SQLAlchemy naming
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)

class Catalogue(db.Model, SerializerMixin):
    __tablename__ = "catalogues"
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.Text, nullable=False)
    brand = db.Column(db.Text, nullable=False)
    model = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    price = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.Text, nullable=False)
    addcatalogues = db.relationship("AddCatalogue", back_populates="catalogue")
    news = db.relationship("News", back_populates="catalogue")  # Define the news relationship

class AddCatalogue(db.Model, SerializerMixin):
    __tablename__ = "addcatalogues"
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.Text, nullable=False)
    brand = db.Column(db.Text, nullable=False)
    model = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    price = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.Text, nullable=False)
    catalogue_id = db.Column(db.Integer, db.ForeignKey('catalogues.id'))
    catalogue = db.relationship("Catalogue", back_populates="addcatalogues")

class News(db.Model, SerializerMixin):
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    ticket_price = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)
    catalogue_id = db.Column(db.Integer, db.ForeignKey('catalogues.id'))
    catalogue = db.relationship("Catalogue", back_populates="news")
