from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .user import User
from .bus import Bus
from .seat import Seat
from .booking import Booking
from .passenger import Passenger

