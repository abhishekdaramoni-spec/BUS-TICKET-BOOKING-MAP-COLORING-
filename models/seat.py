from . import db

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.Integer, db.ForeignKey('bus.id'), nullable=False)
    seat_number = db.Column(db.String(10), nullable=False)
    seat_type = db.Column(db.String(50), nullable=False) # e.g. Seater, Sleeper
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='available') # available, booked
    graph_color = db.Column(db.Integer, nullable=True) # stores the computed color
