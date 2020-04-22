from dataclasses import dataclass
from datetime import datetime

from models.database import db


@dataclass
class Artist(db.Model):
    __tablename__ = 'Artist'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String, nullable=False)
    city: str = db.Column(db.String(120), nullable=False)
    state: str = db.Column(db.String(120), nullable=False)
    phone: str = db.Column(db.String(120), nullable=True)
    genres: str = db.Column(db.String(120), nullable=False)
    image_link: str = db.Column(db.String(500), nullable=True)
    facebook_link: str = db.Column(db.String(120), nullable=True)
    # ✅ TODO: Implement Show and Artist models, and complete ...
    #  ... all model relationships and properties, as a database migration.
    website: str = db.Column(db.String(120), nullable=True)
    seeking_venue: bool = db.Column(db.Boolean, nullable=False)
    seeking_description: str = db.Column(db.String(500), nullable=True)


# *************************************************************************************
# *************************************************************************************
# *************************************************************************************

@dataclass
class Venue(db.Model):
    __tablename__ = 'Venue'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String, nullable=False)
    city: str = db.Column(db.String(120), nullable=False)
    state: str = db.Column(db.String(120), nullable=False)
    phone: str = db.Column(db.String(120), nullable=True)
    image_link: str = db.Column(db.String(500), nullable=True)
    # ✅ TODO: Implement Show and Venue models, and complete ...
    #  ... all model relationships and properties, as a database migration.
    genres: str = db.Column(db.String(120), nullable=False)
    address: str = db.Column(db.String(120), nullable=False)
    website: str = db.Column(db.String(120), nullable=True)
    facebook_link: str = db.Column(db.String(120), nullable=True)
    seeking_talent: bool = db.Column(db.Boolean, nullable=False)
    seeking_description: str = db.Column(db.String(500), nullable=True)


# *************************************************************************************
# *************************************************************************************
# *************************************************************************************


@dataclass
class Show(db.Model):
    __tablename__ = 'Show'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # ✅ TODO: Implement Show and Venue models, and complete ...
    #  ... all model relationships and properties, as a database migration.
    start_time: datetime = db.Column(db.DateTime)

    # Foreign keys
    venue_id: int = db.Column(db.Integer, db.ForeignKey('Venue.id'), primary_key=True, nullable=False)
    artist_id: int = db.Column(db.Integer, db.ForeignKey('Artist.id'), primary_key=True, nullable=False)

    # Relationships
    venue = db.relationship('Venue', backref=db.backref('shows', cascade='all, delete'))
    artist = db.relationship('Artist', backref=db.backref('shows', cascade='all, delete'))
