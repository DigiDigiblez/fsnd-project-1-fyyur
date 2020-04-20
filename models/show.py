from models.database import db


class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    # ✅ TODO: Implement Show and Venue models, and complete ...
    #  ... all model relationships and properties, as a database migration.
    venue_id = db.Column(db.Integer)
    venue_name = db.Column(db.String(120))
    artist_id = db.Column(db.Integer)
    artist_name = db.Column(db.String(120))
    artist_image_link = db.Column(db.String(120))
    start_time = db.Column(db.DateTime)