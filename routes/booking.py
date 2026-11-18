from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import db, Bus, Seat, Booking
from algorithms.discount_rules import calculate_final_fare
from algorithms.cancellation_rules import calculate_refund
from algorithms.graph_coloring import create_seat_graph, greedy_coloring, has_color_conflict
import uuid
import json

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/seats/<int:bus_id>')
def seats(bus_id):
    bus = Bus.query.get_or_404(bus_id)
    passengers = int(request.args.get('passengers', 1))
    date = request.args.get('date')
    seats_list = Seat.query.filter_by(bus_id=bus_id).all()
    
    # We dynamically recalculate coloring here to prove the algorithm executes
    graph = create_seat_graph(seats_list)
    colors = greedy_coloring(graph)
    
    # Update models just in case
    for seat in seats_list:
        seat.graph_color = colors.get(seat.seat_number, 0)
    db.session.commit()
    
    return render_template('seats.html', bus=bus, seats=seats_list, passengers=passengers, date=date, colors=colors, graph=graph)

@booking_bp.route('/passenger', methods=['POST'])
def passenger():
    if 'user_id' not in session:
        flash("Please login to book tickets", "warning")
        return redirect(url_for('auth.login'))
        
    bus_id = request.form.get('bus_id')
    date = request.form.get('date')
    passengers = int(request.form.get('passengers'))
    selected_seats = request.form.get('selected_seats') # comma separated
    
    bus = Bus.query.get(bus_id)
    # Calculate fares
    fare_details = calculate_final_fare(bus.base_price, passengers, bus.bus_type, date)
    
    session['booking_data'] = {
        'bus_id': bus_id,
        'date': date,
        'passengers': passengers,
        'selected_seats': selected_seats,
        'fare_details': fare_details
    }
    
    return render_template('passenger.html', bus=bus, data=session['booking_data'])

@booking_bp.route('/summary', methods=['POST'])
def summary():
    data = session.get('booking_data')
    if not data:
        return redirect(url_for('main.index'))
    
    # Capture passenger info
    passengers_info = []
    for i in range(data['passengers']):
        passengers_info.append({
            'name': request.form.get(f'name_{i}'),
            'age': request.form.get(f'age_{i}'),
            'gender': request.form.get(f'gender_{i}'),
            'email': request.form.get(f'email_{i}'),
            'phone': request.form.get(f'phone_{i}'),
            'seat': request.form.get(f'seat_{i}')
        })
    data['passengers_info'] = passengers_info
    session['booking_data'] = data
    
    return render_template('summary.html', data=data, bus=Bus.query.get(data['bus_id']))

@booking_bp.route('/payment', methods=['POST'])
def payment():
    data = session.get('booking_data')
    if not data:
        return redirect(url_for('main.index'))
    
    bus_id = data['bus_id']
    selected_seats = data['selected_seats'].split(',')
    
    # Check for double booking
    for s_num in selected_seats:
        seat = Seat.query.filter_by(bus_id=bus_id, seat_number=s_num.strip()).first()
        if seat and seat.status == 'booked':
            flash(f"Seat {seat.seat_number} has already been booked. Please try another seat.", "danger")
            session.pop('booking_data', None)
            return redirect(url_for('main.search'))
    
    # Mark seats as booked
    for s_num in selected_seats:
        seat = Seat.query.filter_by(bus_id=bus_id, seat_number=s_num.strip()).first()
        if seat:
            seat.status = 'booked'
            
    booking = Booking(
        user_id=session['user_id'],
        bus_id=bus_id,
        journey_date=data['date'],
        passenger_count=data['passengers'],
        seat_numbers=data['selected_seats'],
        total_amount=data['fare_details']['final_fare'],
        payment_status='Paid',
        booking_status='Confirmed',
        booking_reference=f"BUS-{uuid.uuid4().hex[:8].upper()}"
    )
    db.session.add(booking)
    db.session.flush() # To get booking.id
    
    from models import Passenger
    for p_info in data.get('passengers_info', []):
        passenger = Passenger(
            booking_id=booking.id,
            name=p_info['name'],
            age=p_info['age'],
            gender=p_info['gender'],
            seat_number=p_info['seat']
        )
        db.session.add(passenger)
        
    db.session.commit()
    
    session.pop('booking_data', None)
    return redirect(url_for('booking.confirmation', booking_id=booking.id))

@booking_bp.route('/confirmation/<int:booking_id>')
def confirmation(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.user_id != session.get('user_id'):
        flash("Unauthorized access. You can only view your own tickets.", "danger")
        return redirect(url_for('booking.my_bookings'))
    return render_template('ticket.html', booking=booking)

@booking_bp.route('/my-bookings')
def my_bookings():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    bookings = Booking.query.filter_by(user_id=session['user_id']).order_by(Booking.id.desc()).all()
    return render_template('bookings.html', bookings=bookings)

@booking_bp.route('/cancel/<int:booking_id>', methods=['POST'])
def cancel(booking_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
        
    booking = Booking.query.get_or_404(booking_id)
    if booking.user_id != session['user_id'] or booking.booking_status == 'Cancelled':
        flash("Invalid action", "danger")
        return redirect(url_for('booking.my_bookings'))
        
    bus = booking.bus
    refund_info = calculate_refund(booking.journey_date, bus.departure_time, booking.total_amount)
    
    if refund_info['cancellation_allowed']:
        booking.booking_status = 'Cancelled'
        # Free up seats
        for s_num in booking.seat_numbers.split(','):
            seat = Seat.query.filter_by(bus_id=bus.id, seat_number=s_num.strip()).first()
            if seat:
                seat.status = 'available'
        db.session.commit()
        flash(refund_info['message'], "success")
    else:
        flash(refund_info['message'], "danger")
        
    return redirect(url_for('booking.my_bookings'))
