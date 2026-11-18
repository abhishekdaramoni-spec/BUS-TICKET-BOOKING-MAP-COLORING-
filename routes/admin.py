from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import db, Bus, Seat, Booking, User

admin_bp = Blueprint('admin', __name__)

@admin_bp.before_request
def require_admin():
    if session.get('role') != 'admin':
        flash("Admin access required", "danger")
        return redirect(url_for('main.index'))

@admin_bp.route('/')
def dashboard():
    total_users = User.query.count()
    total_buses = Bus.query.count()
    total_bookings = Booking.query.count()
    # sum of revenue
    revenue = db.session.query(db.func.sum(Booking.total_amount)).filter_by(booking_status='Confirmed').scalar() or 0
    return render_template('admin/dashboard.html', 
                           users=total_users, buses=total_buses, 
                           bookings=total_bookings, revenue=revenue)

@admin_bp.route('/buses')
def buses():
    all_buses = Bus.query.all()
    return render_template('admin/buses.html', buses=all_buses)

@admin_bp.route('/users')
def users():
    all_users = User.query.all()
    return render_template('admin/users.html', users=all_users)

@admin_bp.route('/bookings')
def bookings():
    all_bookings = Booking.query.order_by(Booking.id.desc()).all()
    return render_template('admin/bookings.html', bookings=all_bookings)

