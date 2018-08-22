from app import db
from sqlalchemy.dialects.postgresql import JSON


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String())
    beacon1 = db.Column(db.String())
    beacon2 = db.Column(db.String())
    beacon3 = db.Column(db.String())

    def __init__(self, place, beacon1, beacon2, beacon3):
        self.place = place
        self.beacon1 = beacon1
        self.beacon2 = beacon2
        self.beacon3 = beacon3

    def __repr__(self):
        return '<id {}>'.format(self.id)