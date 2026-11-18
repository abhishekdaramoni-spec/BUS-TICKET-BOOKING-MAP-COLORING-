from flask import Blueprint, render_template, request
from models import Bus, Seat

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/search')
def search():
    from_city = request.args.get('from')
    to_city = request.args.get('to')
    journey_date = request.args.get('date')
    passengers = request.args.get('passengers')
    
    buses = Bus.query.filter_by(from_city=from_city, to_city=to_city).all()
    # In a real scenario, you'd filter by date and passenger availability too
    return render_template('buses.html', buses=buses, date=journey_date, passengers=passengers)

@main_bp.route('/graph-coloring')
def graph_coloring():
    # Render the graph coloring algorithm explanation page
    # Just grab an example bus to show
    bus = Bus.query.first()
    seats = Seat.query.filter_by(bus_id=bus.id).all() if bus else []
    return render_template('graph_coloring.html', bus=bus, seats=seats)
