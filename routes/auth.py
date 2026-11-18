from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import db, User
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            session['role'] = user.role
            flash("Login successful", "success")
            return redirect(url_for('main.index'))
        else:
            flash("Invalid email or password", "danger")
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(email=email).first():
            flash("Email already exists", "danger")
            return redirect(url_for('auth.register'))
            
        hashed_pw = generate_password_hash(password)
        new_user = User(name=name, email=email, password_hash=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please login.", "success")
        return redirect(url_for('auth.login'))
        
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully", "success")
    return redirect(url_for('main.index'))

@auth_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        flash("Please login to view your profile.", "warning")
        return redirect(url_for('auth.login'))
        
    user = User.query.get(session['user_id'])
    if not user:
        session.clear()
        flash("Session expired or user deleted. Please login again.", "danger")
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_email = request.form.get('email')
        
        if new_email != user.email:
            existing = User.query.filter_by(email=new_email).first()
            if existing:
                flash("Email already in use.", "danger")
                return redirect(url_for('auth.profile'))
        
        user.name = new_name
        user.email = new_email
        db.session.commit()
        session['user_name'] = user.name
        flash("Profile updated successfully.", "success")
        return redirect(url_for('auth.profile'))
        
    from models import Booking
    total_bookings = Booking.query.filter_by(user_id=user.id).count()
    upcoming_trips = Booking.query.filter_by(user_id=user.id, booking_status='Confirmed').count()
    completed_trips = 0 # Can be calculated based on journey date
    
    return render_template('profile.html', user=user, total=total_bookings, upcoming=upcoming_trips, completed=completed_trips)

