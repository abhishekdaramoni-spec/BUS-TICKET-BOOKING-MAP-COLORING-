from . import db

class Bus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operator = db.Column(db.String(100), nullable=False)
    from_city = db.Column(db.String(100), nullable=False)
    to_city = db.Column(db.String(100), nullable=False)
    departure_time = db.Column(db.String(50), nullable=False)
    arrival_time = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    bus_type = db.Column(db.String(50), nullable=False) # AC, Non-AC, Sleeper, AC Sleeper
    base_price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, default=0.0)
    amenities = db.Column(db.String(200)) # comma separated
    seats = db.relationship('Seat', backref='bus', lazy=True)
    bookings = db.relationship('Booking', backref='bus', lazy=True)
