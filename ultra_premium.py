import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# 1. Advanced CSS
write_file("static/css/style.css", """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --primary: #d84e55; /* AbhiBus-like red/coral for high conversion */
    --primary-dark: #b83d44;
    --secondary: #182135; /* Deep rich navy for text and contrast */
    --accent: #FFC107;
    --success: #00c46a;
    --danger: #ff4d4d;
    --bg-main: #f4f5f8;
    --text-dark: #182135;
    --text-muted: #6b7280;
    --border-color: #e5e7eb;
    --card-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    --hover-shadow: 0 12px 32px rgba(216, 78, 85, 0.15);
    
    /* Graph Colors */
    --color-0: #fce7f3; /* pink */
    --color-1: #fef3c7; /* amber */
    --color-2: #d1fae5; /* green */
    --color-3: #e0e7ff; /* indigo */
}

body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background-color: var(--bg-main);
    color: var(--text-dark);
    -webkit-font-smoothing: antialiased;
}

/* Navbar */
.navbar {
    background-color: white !important;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    padding: 1rem 0;
}

.navbar-brand {
    font-weight: 800;
    font-size: 1.5rem;
    color: var(--primary) !important;
    letter-spacing: -0.5px;
}

.nav-link {
    color: var(--secondary) !important;
    font-weight: 600;
    font-size: 0.95rem;
    margin: 0 0.5rem;
    transition: color 0.2s;
}

.nav-link:hover {
    color: var(--primary) !important;
}

/* Hero Section */
.hero-wrapper {
    background: linear-gradient(135deg, var(--secondary) 0%, #2a3754 100%);
    padding: 5rem 0 8rem 0;
    position: relative;
    color: white;
    text-align: center;
}

/* Search Widget (Overlapping) */
.search-widget-container {
    margin-top: -4rem;
    position: relative;
    z-index: 10;
}

.search-widget {
    background: white;
    border-radius: 16px;
    padding: 1rem;
    box-shadow: var(--card-shadow);
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0;
}

.search-input-group {
    flex: 1;
    min-width: 200px;
    padding: 1rem 1.5rem;
    border-right: 1px solid var(--border-color);
    position: relative;
}

.search-input-group:last-of-type {
    border-right: none;
}

.search-input-group label {
    font-size: 0.8rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 0.2rem;
    display: block;
}

.search-input-group select, 
.search-input-group input {
    border: none;
    padding: 0;
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--secondary);
    background: transparent;
    box-shadow: none !important;
    outline: none;
    width: 100%;
}

.search-btn {
    background-color: var(--primary);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 1.2rem 2rem;
    font-size: 1.1rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.3s ease;
    height: 100%;
    width: 100%;
}

.search-btn:hover {
    background-color: var(--primary-dark);
    box-shadow: var(--hover-shadow);
}

/* Bus Cards */
.bus-card {
    background: white;
    border-radius: 16px;
    border: 1px solid var(--border-color);
    transition: all 0.3s ease;
    margin-bottom: 1.5rem;
}

.bus-card:hover {
    box-shadow: var(--card-shadow);
    border-color: transparent;
}

.timeline-view {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
}

.time-box {
    text-align: center;
}

.duration-line {
    flex: 1;
    height: 2px;
    background: var(--border-color);
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}

.duration-text {
    background: white;
    padding: 0 10px;
    font-size: 0.8rem;
    color: var(--text-muted);
    font-weight: 600;
}

.duration-line::before, .duration-line::after {
    content: '';
    width: 6px;
    height: 6px;
    background: var(--border-color);
    border-radius: 50%;
    position: absolute;
}
.duration-line::before { left: 0; }
.duration-line::after { right: 0; }

/* Amenities */
.amenity-icon {
    color: var(--text-muted);
    margin-right: 0.8rem;
    font-size: 1.1rem;
}

/* Seat Selection */
.bus-interior {
    background: white;
    border: 2px solid var(--border-color);
    border-radius: 20px;
    padding: 2rem;
    width: fit-content;
    margin: 0 auto;
    position: relative;
}

.steering-wheel {
    position: absolute;
    top: 2rem;
    right: 2rem;
    font-size: 2rem;
    color: var(--text-muted);
}

.seat-btn {
    width: 45px;
    height: 55px;
    border-radius: 8px 8px 4px 4px;
    border: 2px solid #cbd5e1;
    background: white;
    font-weight: 700;
    font-size: 0.8rem;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s;
    margin-bottom: 0.5rem;
}

.seat-btn:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.seat-booked {
    background-color: #cbd5e1 !important;
    border-color: #94a3b8 !important;
    color: white;
    cursor: not-allowed;
    opacity: 0.6;
}

.seat-selected {
    background-color: var(--success) !important;
    border-color: #059669 !important;
    color: white !important;
}

.seat-row {
    display: flex;
    gap: 10px;
}

.aisle {
    width: 30px; /* Aisle spacing */
}

/* Buttons */
.btn-primary-custom {
    background-color: var(--primary);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    padding: 0.75rem 1.5rem;
}
.btn-primary-custom:hover {
    background-color: var(--primary-dark);
}

.price-text {
    font-size: 1.6rem;
    font-weight: 800;
    color: var(--secondary);
}

/* Footer */
.footer {
    background-color: var(--secondary);
    color: white;
    padding: 4rem 0 2rem 0;
    margin-top: 5rem;
}
""")

# 2. Update base.html
write_file("templates/base.html", """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BusGo | Premium Bus Booking</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="/static/css/style.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg sticky-top">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('main.index') }}">BUS<span style="color: var(--secondary) !important;">GO</span></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto ms-4">
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('main.index') }}">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('main.graph_coloring') }}"><i class="fa-solid fa-brain text-primary me-1"></i>Algorithm Details</a></li>
                </ul>
                <ul class="navbar-nav align-items-center">
                    {% if session.get('user_id') %}
                        {% if session.get('role') == 'admin' %}
                            <li class="nav-item"><a class="nav-link text-danger fw-bold" href="{{ url_for('admin.dashboard') }}">Admin</a></li>
                        {% endif %}
                        <li class="nav-item"><a class="nav-link" href="{{ url_for('auth.profile') }}"><i class="fa-regular fa-user me-1"></i> Profile</a></li>
                        <li class="nav-item"><a class="nav-link" href="{{ url_for('booking.my_bookings') }}"><i class="fa-solid fa-ticket me-1"></i> My Bookings</a></li>
                        <li class="nav-item ms-3"><a class="btn btn-outline-dark btn-sm rounded-pill px-3 fw-bold" href="{{ url_for('auth.logout') }}">Logout</a></li>
                    {% else %}
                        <li class="nav-item"><a class="nav-link" href="{{ url_for('auth.login') }}">Login</a></li>
                        <li class="nav-item ms-3"><a class="btn btn-primary-custom rounded-pill px-4" href="{{ url_for('auth.register') }}">Sign Up</a></li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>
    
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <div class="container mt-4 position-absolute start-50 translate-middle-x" style="z-index: 1050;">
            {% for category, message in messages %}
                <div class="alert alert-{{ category }} alert-dismissible fade show shadow border-0" role="alert">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            {% endfor %}
            </div>
        {% endif %}
    {% endwith %}
    
    {% block content %}{% endblock %}
    
    <footer class="footer">
        <div class="container">
            <div class="row">
                <div class="col-md-4 mb-4">
                    <h3 class="fw-bold mb-3">BUSGO</h3>
                    <p class="text-white-50">India's most advanced bus ticketing platform, powered by Graph Coloring algorithms.</p>
                </div>
                <div class="col-md-2 mb-4">
                    <h5 class="mb-3">Quick Links</h5>
                    <ul class="list-unstyled text-white-50">
                        <li><a href="#" class="text-white-50 text-decoration-none">About Us</a></li>
                        <li><a href="#" class="text-white-50 text-decoration-none">Offers</a></li>
                        <li><a href="#" class="text-white-50 text-decoration-none">Careers</a></li>
                    </ul>
                </div>
            </div>
            <hr class="border-secondary">
            <div class="text-center text-white-50 small mt-3">
                &copy; 2026 BusGo Platform. All rights reserved. (Academic Project)
            </div>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="/static/js/main.js"></script>
</body>
</html>
""")

# 3. Update index.html
write_file("templates/index.html", """
{% extends 'base.html' %}
{% block content %}
<div class="hero-wrapper">
    <div class="container">
        <h1 class="display-3 fw-bold mb-3 tracking-tight">Book Your Perfect Journey.</h1>
        <p class="fs-4 text-white-50 mb-0">Experience premium travel with our smart seat allocation system.</p>
    </div>
</div>

<div class="container search-widget-container mb-5">
    <div class="search-widget">
        <form action="{{ url_for('main.search') }}" method="GET" class="w-100 d-flex flex-column flex-lg-row">
            <div class="search-input-group">
                <label><i class="fa-solid fa-location-dot text-primary me-2"></i> From</label>
                <select name="from" required>
                    <option value="Ahmedabad">Ahmedabad</option>
                    <option value="Rajkot">Rajkot</option>
                    <option value="Surat">Surat</option>
                    <option value="Vadodara">Vadodara</option>
                    <option value="Mumbai">Mumbai</option>
                </select>
            </div>
            <div class="search-input-group">
                <label><i class="fa-solid fa-location-dot text-primary me-2"></i> To</label>
                <select name="to" required>
                    <option value="Rajkot">Rajkot</option>
                    <option value="Ahmedabad">Ahmedabad</option>
                    <option value="Surat">Surat</option>
                    <option value="Mumbai">Mumbai</option>
                </select>
            </div>
            <div class="search-input-group">
                <label><i class="fa-regular fa-calendar text-primary me-2"></i> Date of Journey</label>
                <input type="date" name="date" required>
            </div>
            <div class="search-input-group">
                <label><i class="fa-solid fa-users text-primary me-2"></i> Passengers</label>
                <input type="number" name="passengers" min="1" max="6" value="1" required>
            </div>
            <div class="p-2" style="flex: 0 0 200px;">
                <button type="submit" class="search-btn">Search Buses</button>
            </div>
        </form>
    </div>
</div>

<div class="container mt-5 pt-4">
    <h3 class="fw-bold mb-4">Why BusGo is Better</h3>
    <div class="row g-4">
        <div class="col-md-4">
            <div class="card h-100 border-0 shadow-sm p-4" style="border-radius: 16px;">
                <i class="fa-solid fa-bolt text-warning fs-1 mb-3"></i>
                <h5 class="fw-bold">Lightning Fast Booking</h5>
                <p class="text-muted mb-0">Our streamlined flow lets you book tickets in under a minute with seamless mock payments.</p>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card h-100 border-0 shadow-sm p-4" style="border-radius: 16px;">
                <i class="fa-solid fa-network-wired text-primary fs-1 mb-3"></i>
                <h5 class="fw-bold">Smart Graph Seats</h5>
                <p class="text-muted mb-0">Unlike generic sites, we use Greedy Graph Coloring to logically group and allocate seats.</p>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card h-100 border-0 shadow-sm p-4" style="border-radius: 16px;">
                <i class="fa-solid fa-shield-check text-success fs-1 mb-3"></i>
                <h5 class="fw-bold">100% Secure</h5>
                <p class="text-muted mb-0">Robust Flask sessions, Werkzeug password hashing, and strict data isolation per user.</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""")

# 4. Update buses.html
write_file("templates/buses.html", """
{% extends 'base.html' %}
{% block content %}
<div class="container mt-4">
    <div class="d-flex justify-content-between align-items-end mb-4 border-bottom pb-3">
        <div>
            <h2 class="fw-bold mb-1">{{ request.args.get('from') }} <i class="fa-solid fa-arrow-right mx-2 text-muted fs-4"></i> {{ request.args.get('to') }}</h2>
            <p class="text-muted mb-0 fw-semibold">{{ date }} &bull; {{ passengers }} Passenger(s)</p>
        </div>
        <div>
            <span class="badge bg-success bg-opacity-10 text-success border border-success fs-6 px-3 py-2 rounded-pill">{{ buses|length }} Buses Found</span>
        </div>
    </div>

    <div class="row">
        <!-- Sidebar -->
        <div class="col-lg-3 mb-4">
            <div class="card shadow-sm border-0" style="border-radius: 16px; position: sticky; top: 100px;">
                <div class="card-body p-4">
                    <h5 class="fw-bold mb-4">Filters</h5>
                    
                    <h6 class="fw-bold small text-muted text-uppercase mb-3">Bus Type</h6>
                    <div class="form-check mb-2">
                        <input class="form-check-input" type="checkbox" checked>
                        <label class="form-check-label fw-semibold">AC</label>
                    </div>
                    <div class="form-check mb-2">
                        <input class="form-check-input" type="checkbox" checked>
                        <label class="form-check-label fw-semibold">Non-AC</label>
                    </div>
                    <div class="form-check mb-4">
                        <input class="form-check-input" type="checkbox" checked>
                        <label class="form-check-label fw-semibold">Sleeper</label>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Results -->
        <div class="col-lg-9">
            {% for bus in buses %}
            <div class="bus-card p-4">
                <div class="row align-items-center">
                    <div class="col-md-3 border-end">
                        <h4 class="fw-bold mb-1">{{ bus.operator }}</h4>
                        <span class="badge bg-light text-dark border">{{ bus.bus_type }}</span>
                        <div class="mt-2 text-warning fw-bold small"><i class="fa-solid fa-star"></i> {{ bus.rating }}</div>
                    </div>
                    
                    <div class="col-md-6 px-4">
                        <div class="timeline-view">
                            <div class="time-box">
                                <h4 class="fw-bold mb-0">{{ bus.departure_time }}</h4>
                                <small class="text-muted fw-semibold">{{ bus.from_city }}</small>
                            </div>
                            <div class="duration-line"><span class="duration-text">{{ bus.duration }}</span></div>
                            <div class="time-box">
                                <h4 class="fw-bold mb-0">{{ bus.arrival_time }}</h4>
                                <small class="text-muted fw-semibold">{{ bus.to_city }}</small>
                            </div>
                        </div>
                        <div class="mt-3 text-center">
                            <i class="fa-solid fa-wifi amenity-icon" title="WiFi"></i>
                            <i class="fa-solid fa-plug amenity-icon" title="Charging"></i>
                            <i class="fa-solid fa-bottle-water amenity-icon" title="Water"></i>
                        </div>
                    </div>
                    
                    <div class="col-md-3 text-md-end mt-3 mt-md-0 border-start ps-md-4">
                        <p class="text-muted small mb-1">Starting from</p>
                        <div class="price-text mb-3">₹{{ bus.base_price }}</div>
                        <a href="{{ url_for('booking.seats', bus_id=bus.id, date=date, passengers=passengers) }}" class="btn btn-primary-custom w-100">Select Seats</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</div>
{% endblock %}
""")

# 5. Update seats.html
write_file("templates/seats.html", """
{% extends 'base.html' %}
{% block content %}
<div class="container mt-4">
    <div class="row">
        <!-- Seat Map Area -->
        <div class="col-lg-7 mb-4">
            <h3 class="fw-bold mb-3">Select Your Seats</h3>
            <div class="d-flex gap-3 mb-4 flex-wrap">
                <div class="d-flex align-items-center"><div style="width:16px; height:16px; background:#fff; border:2px solid #cbd5e1; border-radius:4px; margin-right:8px;"></div><small class="fw-semibold">Available</small></div>
                <div class="d-flex align-items-center"><div style="width:16px; height:16px; background:#cbd5e1; border-radius:4px; margin-right:8px;"></div><small class="fw-semibold">Booked</small></div>
                <div class="d-flex align-items-center"><div style="width:16px; height:16px; background:var(--success); border-radius:4px; margin-right:8px;"></div><small class="fw-semibold">Selected</small></div>
            </div>
            
            <div class="alert alert-light border shadow-sm mb-4">
                <h6 class="fw-bold text-primary mb-2"><i class="fa-solid fa-brain me-2"></i>Graph Coloring Active</h6>
                <p class="small mb-2 text-muted">Seats are dynamically assigned to Allocation Groups to prevent adjacency conflicts.</p>
                <div class="d-flex gap-2">
                    <span class="badge" style="background-color: var(--color-0); color: #000;">Grp A</span>
                    <span class="badge" style="background-color: var(--color-1); color: #000;">Grp B</span>
                    <span class="badge" style="background-color: var(--color-2); color: #000;">Grp C</span>
                    <span class="badge" style="background-color: var(--color-3); color: #000;">Grp D</span>
                </div>
            </div>

            <div class="bus-interior shadow-sm">
                <i class="fa-solid fa-steering-wheel steering-wheel"></i>
                <div class="text-end mb-4 border-bottom pb-2 text-muted fw-bold small">FRONT</div>
                
                <div class="d-flex flex-column gap-2 align-items-center">
                    {% set rows = ['A', 'B', 'C', 'D', 'E'] %}
                    {% for r in rows %}
                    <div class="seat-row">
                        <!-- Left side seats (1, 2) -->
                        {% for c in ['1', '2'] %}
                            {% set s_num = r ~ c %}
                            {% set seat = seats | selectattr("seat_number", "equalto", s_num) | first %}
                            {% if seat %}
                                {% set bg_color = 'var(--color-' ~ seat.graph_color ~ ')' if seat.status == 'available' else '' %}
                                <button class="seat-btn {% if seat.status == 'booked' %}seat-booked{% endif %}" 
                                        data-seat="{{ seat.seat_number }}" data-status="{{ seat.status }}" data-color="{{ bg_color }}"
                                        style="{% if seat.status == 'available' %}background-color: {{ bg_color }};{% endif %}">
                                    {{ seat.seat_number }}
                                </button>
                            {% else %}
                                <div style="width:45px;"></div>
                            {% endif %}
                        {% endfor %}
                        
                        <!-- Aisle -->
                        <div class="aisle"></div>
                        
                        <!-- Right side seats (3, 4) -->
                        {% for c in ['3', '4'] %}
                            {% set s_num = r ~ c %}
                            {% set seat = seats | selectattr("seat_number", "equalto", s_num) | first %}
                            {% if seat %}
                                {% set bg_color = 'var(--color-' ~ seat.graph_color ~ ')' if seat.status == 'available' else '' %}
                                <button class="seat-btn {% if seat.status == 'booked' %}seat-booked{% endif %}" 
                                        data-seat="{{ seat.seat_number }}" data-status="{{ seat.status }}" data-color="{{ bg_color }}"
                                        style="{% if seat.status == 'available' %}background-color: {{ bg_color }};{% endif %}">
                                    {{ seat.seat_number }}
                                </button>
                            {% else %}
                                <div style="width:45px;"></div>
                            {% endif %}
                        {% endfor %}
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>

        <!-- Summary Area -->
        <div class="col-lg-5">
            <div class="card shadow-sm border-0" style="border-radius: 16px; position: sticky; top: 100px;">
                <div class="card-body p-4">
                    <h4 class="fw-bold mb-4">Boarding & Dropping</h4>
                    <div class="d-flex justify-content-between mb-3 border-bottom pb-3">
                        <div>
                            <h6 class="fw-bold mb-1">{{ bus.from_city }}</h6>
                            <p class="text-muted small mb-0">{{ bus.departure_time }}</p>
                        </div>
                        <div class="text-end">
                            <h6 class="fw-bold mb-1">{{ bus.to_city }}</h6>
                            <p class="text-muted small mb-0">{{ bus.arrival_time }}</p>
                        </div>
                    </div>
                    
                    <div class="d-flex justify-content-between mb-3">
                        <span class="text-muted fw-semibold">Seats Selected</span>
                        <span id="selected-list" class="fw-bold">None</span>
                    </div>
                    <div class="d-flex justify-content-between mb-4">
                        <span class="text-muted fw-semibold">Required</span>
                        <span id="passenger-count" class="fw-bold">{{ passengers }}</span>
                    </div>
                    
                    <div class="d-flex justify-content-between align-items-center mb-4 pt-3 border-top">
                        <span class="fs-5 fw-bold">Total Amount</span>
                        <span class="fs-4 fw-bold text-primary" id="temp-total">₹0</span>
                    </div>
                    
                    <form action="{{ url_for('booking.passenger') }}" method="POST" id="seat-form">
                        <input type="hidden" name="bus_id" value="{{ bus.id }}">
                        <input type="hidden" name="date" value="{{ date }}">
                        <input type="hidden" name="passengers" id="passengers-input" value="{{ passengers }}">
                        <input type="hidden" name="selected_seats" id="selected-seats-input">
                        <button type="submit" class="btn btn-primary-custom w-100" id="continue-btn" disabled>Proceed to Passenger Details</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    const maxPassengers = parseInt(document.getElementById('passenger-count').innerText);
    const basePrice = {{ bus.base_price }};
    let selectedSeats = [];

    document.querySelectorAll('.seat-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            if (this.dataset.status === 'booked') return;

            const seatNum = this.dataset.seat;
            const originalColor = this.dataset.color;
            
            if (selectedSeats.includes(seatNum)) {
                // Deselect
                selectedSeats = selectedSeats.filter(s => s !== seatNum);
                this.classList.remove('seat-selected');
                this.style.backgroundColor = originalColor;
            } else {
                // Select
                if (selectedSeats.length >= maxPassengers) {
                    alert('Maximum seats selected.');
                    return;
                }
                selectedSeats.push(seatNum);
                this.classList.add('seat-selected');
                this.style.backgroundColor = ''; // CSS class takes over
            }
            
            document.getElementById('selected-list').innerText = selectedSeats.length > 0 ? selectedSeats.join(', ') : 'None';
            document.getElementById('selected-seats-input').value = selectedSeats.join(',');
            document.getElementById('temp-total').innerText = '₹' + (selectedSeats.length * basePrice);
            document.getElementById('continue-btn').disabled = selectedSeats.length !== maxPassengers;
        });
    });
</script>
{% endblock %}
""")

print("Ultra Premium Scripts Generated.")
