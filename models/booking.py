from . import db
from datetime import datetime

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bus_id = db.Column(db.Integer, db.ForeignKey('bus.id'), nullable=False)
    journey_date = db.Column(db.String(50), nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    passenger_count = db.Column(db.Integer, nullable=False)
    seat_numbers = db.Column(db.String(200), nullable=False) # comma separated
    total_amount = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(50), default='Pending')
    booking_status = db.Column(db.String(50), default='Confirmed') # Confirmed, Cancelled
    booking_reference = db.Column(db.String(50), unique=True, nullable=False)
    passengers_list = db.relationship('Passenger', backref='booking', lazy=True)
