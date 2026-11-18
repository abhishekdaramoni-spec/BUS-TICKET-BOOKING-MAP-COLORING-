import os

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

write_file("templates/base.html", """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BusGo - Graph Coloring Bus Tickets</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/static/css/style.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand fw-bold" href="{{ url_for('main.index') }}">BusGo</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('main.index') }}">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('main.graph_coloring') }}">Algorithm Details</a></li>
                </ul>
                <ul class="navbar-nav">
                    {% if session.get('user_id') %}
                        {% if session.get('role') == 'admin' %}
                            <li class="nav-item"><a class="nav-link" href="{{ url_for('admin.dashboard') }}">Admin</a></li>
                        {% endif %}
                        <li class="nav-item"><a class="nav-link" href="{{ url_for('booking.my_bookings') }}">My Bookings</a></li>
                        <li class="nav-item"><a class="nav-link" href="{{ url_for('auth.logout') }}">Logout</a></li>
                    {% else %}
                        <li class="nav-item"><a class="nav-link" href="{{ url_for('auth.login') }}">Login</a></li>
                        <li class="nav-item"><a class="nav-link" href="{{ url_for('auth.register') }}">Register</a></li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>
    <div class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
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

write_file("templates/index.html", """
{% extends 'base.html' %}
{% block content %}
<div class="p-5 mb-4 bg-light rounded-3 text-center hero-section">
    <div class="container-fluid py-5">
        <h1 class="display-5 fw-bold">Book Your Journey With Ease</h1>
        <p class="col-md-8 mx-auto fs-4">Find comfortable buses using our advanced Graph-Coloring seat allocation system.</p>
        
        <div class="card mt-4 shadow-sm mx-auto" style="max-width: 800px;">
            <div class="card-body">
                <form action="{{ url_for('main.search') }}" method="GET" class="row g-3">
                    <div class="col-md-3">
                        <label class="form-label">From</label>
                        <select name="from" class="form-select" required>
                            <option value="Ahmedabad">Ahmedabad</option>
                            <option value="Rajkot">Rajkot</option>
                            <option value="Surat">Surat</option>
                            <option value="Vadodara">Vadodara</option>
                        </select>
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">To</label>
                        <select name="to" class="form-select" required>
                            <option value="Rajkot">Rajkot</option>
                            <option value="Ahmedabad">Ahmedabad</option>
                            <option value="Surat">Surat</option>
                            <option value="Mumbai">Mumbai</option>
                        </select>
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Journey Date</label>
                        <input type="date" name="date" class="form-control" required>
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Passengers</label>
                        <input type="number" name="passengers" class="form-control" min="1" value="1" required>
                    </div>
                    <div class="col-12 text-center mt-4">
                        <button type="submit" class="btn btn-primary btn-lg px-5">Search Buses</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""")

write_file("templates/buses.html", """
{% extends 'base.html' %}
{% block content %}
<h2>Available Buses</h2>
<p class="text-muted">{{ request.args.get('from') }} to {{ request.args.get('to') }} | {{ date }} | {{ passengers }} Passenger(s)</p>
<div class="row">
    {% for bus in buses %}
    <div class="col-md-12 mb-3">
        <div class="card shadow-sm">
            <div class="card-body d-flex justify-content-between align-items-center">
                <div>
                    <h5 class="card-title">{{ bus.operator }} <span class="badge bg-secondary">{{ bus.bus_type }}</span></h5>
                    <p class="mb-1 fw-bold">{{ bus.departure_time }} &rarr; {{ bus.arrival_time }}</p>
                    <p class="text-muted small mb-0">{{ bus.duration }} | Rating: {{ bus.rating }} | Amenities: {{ bus.amenities }}</p>
                </div>
                <div class="text-end">
                    <h4 class="text-primary mb-3">₹{{ bus.base_price }}</h4>
                    <a href="{{ url_for('booking.seats', bus_id=bus.id, date=date, passengers=passengers) }}" class="btn btn-outline-primary">Select Seats</a>
                </div>
            </div>
        </div>
    </div>
    {% else %}
    <div class="col-12">
        <div class="alert alert-warning">No buses found for this route.</div>
    </div>
    {% endfor %}
</div>
{% endblock %}
""")

print("HTML bootstrap 1 complete.")
