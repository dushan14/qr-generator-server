from app import db
from sqlalchemy.dialects.postgresql import JSON


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String())
    beacon1 = db.Column(db.String())
    beacon2 = db.Column(db.String())
    beacon3 = db.Column(db.String())
    beacon1x = db.Column(db.String)
    beacon1y = db.Column(db.String)
    beacon2x = db.Column(db.String)
    beacon2y = db.Column(db.String)
    beacon3x = db.Column(db.String)
    beacon3y = db.Column(db.String)

    def __init__(self, place, beacon1,beacon1x,beacon1y,beacon2,beacon2x,beacon2y,beacon3,beacon3x,beacon3y):
        self.place = place
        
        self.beacon1 = beacon1
        self.beacon1x = beacon1x
        self.beacon1y = beacon1y

        self.beacon2 = beacon2
        self.beacon2x = beacon2x
        self.beacon2y = beacon2y

        self.beacon3 = beacon3
        self.beacon3x = beacon3x
        self.beacon3y = beacon3y


    def __repr__(self):
        return '<id {}>'.format(self.id)