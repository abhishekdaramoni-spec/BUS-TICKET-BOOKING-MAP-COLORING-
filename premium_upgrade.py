import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# 1. Update CSS for Premium UI
write_file("static/css/style.css", """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --primary: #0A2540; /* Deep navy */
    --accent: #00E5FF; /* Teal/Cyan */
    --success: #00D09C;
    --danger: #FF5A5F;
    --warning: #FFB400;
    --bg-light: #F7F9FC;
    --text-dark: #0F172A;
    --card-shadow: 0 10px 25px rgba(0,0,0,0.05);
    
    /* Graph Colors */
    --color-0: #FFE4E6;
    --color-1: #FEF3C7;
    --color-2: #D1FAE5;
    --color-3: #DBEAFE;
    --color-4: #F3E8FF;
    --color-5: #FFEDD5;
}

body {
    font-family: 'Inter', sans-serif;
    background-color: var(--bg-light);
    color: var(--text-dark);
    -webkit-font-smoothing: antialiased;
}

.navbar {
    background-color: var(--primary) !important;
    padding: 1rem 0;
}

.navbar-brand {
    font-weight: 700;
    letter-spacing: 1px;
    color: white !important;
}

.navbar-brand span {
    color: var(--accent);
}

.hero-section {
    background: linear-gradient(135deg, var(--primary) 0%, #1e3a8a 100%);
    color: white;
    padding: 6rem 0;
    position: relative;
    overflow: hidden;
}

.hero-section::after {
    content: '';
    position: absolute;
    right: -10%;
    top: -20%;
    width: 50%;
    height: 150%;
    background: radial-gradient(circle, rgba(0,229,255,0.1) 0%, rgba(0,0,0,0) 70%);
    z-index: 0;
}

.search-card {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    position: relative;
    z-index: 1;
    transform: translateY(3rem);
}

.card {
    border: none;
    border-radius: 12px;
    box-shadow: var(--card-shadow);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.08);
}

.btn-primary {
    background-color: var(--primary);
    border-color: var(--primary);
    border-radius: 8px;
    font-weight: 500;
    padding: 0.6rem 1.5rem;
}

.btn-primary:hover {
    background-color: #1e3a8a;
    border-color: #1e3a8a;
}

.btn-accent {
    background-color: var(--accent);
    color: var(--primary);
    border: none;
    font-weight: 600;
    border-radius: 8px;
}

.btn-accent:hover {
    background-color: #00b4d8;
    color: white;
}

.floating-badge {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 20px;
    padding: 0.5rem 1rem;
    display: inline-block;
    font-size: 0.9rem;
    margin-right: 1rem;
    margin-bottom: 1rem;
}

.bus-layout {
    background: white;
    border: 2px solid #E2E8F0;
    border-radius: 16px;
}

.driver-seat {
    border-bottom: 2px dashed #CBD5E1;
    padding-bottom: 1rem;
    margin-bottom: 2rem !important;
}

.seat-btn {
    border-radius: 8px 8px 4px 4px; /* Looks more like a seat */
    font-weight: 600;
    border: 2px solid transparent;
    transition: all 0.2s;
}

.seat-btn:hover:not(.disabled) {
    transform: scale(1.05);
}

.feature-icon {
    font-size: 2.5rem;
    color: var(--accent);
    margin-bottom: 1rem;
}
""")

# 2. Update Index Page
write_file("templates/index.html", """
{% extends 'base.html' %}
{% block content %}
</div> <!-- Close container to allow full width hero -->

<div class="hero-section text-center text-md-start">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-md-7 position-relative" style="z-index: 1;">
                <span class="text-uppercase tracking-wide text-info fw-bold mb-2 d-block" style="letter-spacing: 2px; color: var(--accent) !important;">Premium Travel Experience</span>
                <h1 class="display-4 fw-bold mb-4">Book Your Journey With Ease</h1>
                <p class="fs-5 mb-5 text-light opacity-75">Find buses, choose your perfect seat using our Graph-Coloring algorithm, and travel with confidence.</p>
                
                <div>
                    <span class="floating-badge">🛣️ 10+ Routes</span>
                    <span class="floating-badge">💺 500+ Seats</span>
                    <span class="floating-badge">🔒 Secure Payments</span>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="container" style="margin-top: -80px; position: relative; z-index: 10;">
    <div class="search-card">
        <form action="{{ url_for('main.search') }}" method="GET" class="row g-3 align-items-end">
            <div class="col-md-3">
                <label class="form-label text-muted fw-semibold small text-uppercase">From</label>
                <select name="from" class="form-select form-select-lg border-0 bg-light" required>
                    <option value="Ahmedabad">Ahmedabad</option>
                    <option value="Rajkot">Rajkot</option>
                    <option value="Surat">Surat</option>
                    <option value="Vadodara">Vadodara</option>
                </select>
            </div>
            <div class="col-md-3">
                <label class="form-label text-muted fw-semibold small text-uppercase">To</label>
                <select name="to" class="form-select form-select-lg border-0 bg-light" required>
                    <option value="Rajkot">Rajkot</option>
                    <option value="Ahmedabad">Ahmedabad</option>
                    <option value="Surat">Surat</option>
                    <option value="Mumbai">Mumbai</option>
                </select>
            </div>
            <div class="col-md-3">
                <label class="form-label text-muted fw-semibold small text-uppercase">Journey Date</label>
                <input type="date" name="date" class="form-control form-control-lg border-0 bg-light" required>
            </div>
            <div class="col-md-2">
                <label class="form-label text-muted fw-semibold small text-uppercase">Passengers</label>
                <input type="number" name="passengers" class="form-control form-control-lg border-0 bg-light" min="1" max="6" value="1" required>
            </div>
            <div class="col-md-1 text-end">
                <button type="submit" class="btn btn-accent btn-lg w-100 h-100 d-flex align-items-center justify-content-center">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                </button>
            </div>
        </form>
    </div>
</div>

<div class="container mt-5 pt-5 mb-5">
    <div class="text-center mb-5">
        <h2 class="fw-bold">Why Choose BUSGO?</h2>
        <p class="text-muted">Premium service backed by advanced algorithms</p>
    </div>
    <div class="row g-4">
        <div class="col-md-3">
            <div class="card h-100 p-4 text-center">
                <div class="feature-icon">🚀</div>
                <h5>Easy Booking</h5>
                <p class="text-muted small mb-0">Book your premium seat in minutes with our streamlined flow.</p>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card h-100 p-4 text-center">
                <div class="feature-icon">🧠</div>
                <h5>Smart Seats</h5>
                <p class="text-muted small mb-0">Interactive graph-powered seat allocation ensures optimal grouping.</p>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card h-100 p-4 text-center">
                <div class="feature-icon">🔒</div>
                <h5>Secure</h5>
                <p class="text-muted small mb-0">Your account and booking information stay protected.</p>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card h-100 p-4 text-center">
                <div class="feature-icon">📱</div>
                <h5>Digital Ticket</h5>
                <p class="text-muted small mb-0">Get your ticket and QR code instantly after booking.</p>
            </div>
        </div>
    </div>
</div>

<div class="container pb-5"> <!-- Reopen container for base.html structure -->
{% endblock %}
""")

# 3. Update Base HTML for Brand
write_file("templates/base.html", """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BUSGO | Your Journey. Your Seat. Your Way.</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/static/css/style.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark sticky-top">
        <div class="container">
            <a class="navbar-brand fs-3" href="{{ url_for('main.index') }}">BUS<span>GO</span></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto ms-4">
                    <li class="nav-item"><a class="nav-link text-white" href="{{ url_for('main.index') }}">Home</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="{{ url_for('main.graph_coloring') }}">How It Works (Algorithm)</a></li>
                </ul>
                <ul class="navbar-nav">
                    {% if session.get('user_id') %}
                        {% if session.get('role') == 'admin' %}
                            <li class="nav-item"><a class="nav-link text-warning fw-bold" href="{{ url_for('admin.dashboard') }}">Admin Dashboard</a></li>
                        {% endif %}
                        <li class="nav-item"><a class="nav-link text-white" href="{{ url_for('auth.profile') }}">Profile</a></li>
                        <li class="nav-item"><a class="nav-link text-white" href="{{ url_for('booking.my_bookings') }}">My Bookings</a></li>
                        <li class="nav-item ms-2"><a class="btn btn-outline-light btn-sm mt-1" href="{{ url_for('auth.logout') }}">Logout</a></li>
                    {% else %}
                        <li class="nav-item"><a class="nav-link text-white" href="{{ url_for('auth.login') }}">Login</a></li>
                        <li class="nav-item ms-2"><a class="btn btn-accent btn-sm mt-1" href="{{ url_for('auth.register') }}">Create Account</a></li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>
    <div class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }} shadow-sm border-0">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        {% block content %}{% endblock %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="/static/js/main.js"></script>
</body>
</html>
""")

# 4. Add Passenger Model
write_file("models/passenger.py", """
from . import db

class Passenger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    seat_number = db.Column(db.String(10), nullable=False)
""")

print("Premium UI and Passenger models generated.")
