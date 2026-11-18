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
                        <li class="nav-item"><a class="nav-link" href="{{ url_for('auth.profile') }}">Profile</a></li>
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

write_file("templates/ticket.html", """
{% extends 'base.html' %}
{% block content %}
<div class="row">
    <div class="col-md-8 mx-auto">
        <div class="card shadow border-success mb-4">
            <div class="card-header bg-success text-white text-center py-3">
                <h3 class="mb-0">✓ Booking Confirmed</h3>
            </div>
            <div class="card-body p-4">
                <div class="d-flex justify-content-between mb-4 pb-3 border-bottom">
                    <div>
                        <h5 class="text-muted mb-1">BUSGO BUS TICKET</h5>
                        <h4 class="text-primary">{{ booking.booking_reference }}</h4>
                    </div>
                    <div class="text-end">
                        <img src="https://api.qrserver.com/v1/create-qr-code/?size=100x100&data={{ booking.booking_reference }}" alt="QR Code">
                    </div>
                </div>
                
                <div class="row mb-3 pb-3 border-bottom">
                    <div class="col-4"><p class="text-muted mb-0">User ID</p><h5>{{ booking.user.id }}</h5></div>
                    <div class="col-4"><p class="text-muted mb-0">Account Name</p><h5>{{ booking.user.name }}</h5></div>
                    <div class="col-4"><p class="text-muted mb-0">Account Email</p><h5>{{ booking.user.email }}</h5></div>
                </div>

                <div class="row mb-3">
                    <div class="col-6"><p class="text-muted mb-0">Bus Operator</p><h5>{{ booking.bus.operator }}</h5></div>
                    <div class="col-6"><p class="text-muted mb-0">Bus Type</p><h5>{{ booking.bus.bus_type }}</h5></div>
                </div>
                <div class="row mb-3">
                    <div class="col-6"><p class="text-muted mb-0">Route</p><h5>{{ booking.bus.from_city }} &rarr; {{ booking.bus.to_city }}</h5></div>
                    <div class="col-6"><p class="text-muted mb-0">Journey Date</p><h5>{{ booking.journey_date }}</h5></div>
                </div>
                <div class="row mb-3">
                    <div class="col-6"><p class="text-muted mb-0">Seats</p><h5>{{ booking.seat_numbers }}</h5></div>
                    <div class="col-6"><p class="text-muted mb-0">Departure</p><h5>{{ booking.bus.departure_time }}</h5></div>
                </div>
                <div class="row mb-3">
                    <div class="col-6"><p class="text-muted mb-0">Payment</p><h5 class="text-success">{{ booking.payment_status }}</h5></div>
                    <div class="col-6"><p class="text-muted mb-0">Total Paid</p><h5 class="text-success">₹{{ booking.total_amount }}</h5></div>
                </div>
                
                <div class="text-center mt-4">
                    <button class="btn btn-outline-secondary" onclick="window.print()">Print Ticket</button>
                    <a href="{{ url_for('booking.my_bookings') }}" class="btn btn-primary">My Bookings</a>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""")

write_file("templates/profile.html", """
{% extends 'base.html' %}
{% block content %}
<div class="row">
    <div class="col-md-6 mx-auto">
        <h3 class="mb-4">Profile</h3>
        
        <div class="card shadow-sm mb-4">
            <div class="card-body text-center">
                <h5 class="card-title">User ID: {{ user.id }}</h5>
                <hr>
                <div class="d-flex justify-content-around">
                    <div><h4 class="text-primary">{{ total }}</h4><p class="text-muted small">Total Bookings</p></div>
                    <div><h4 class="text-success">{{ upcoming }}</h4><p class="text-muted small">Upcoming Trips</p></div>
                    <div><h4 class="text-secondary">{{ completed }}</h4><p class="text-muted small">Completed Trips</p></div>
                </div>
            </div>
        </div>

        <div class="card shadow-sm">
            <div class="card-body">
                <form method="POST" action="{{ url_for('auth.profile') }}">
                    <div class="mb-3">
                        <label>Name</label>
                        <input type="text" name="name" class="form-control" value="{{ user.name }}" required>
                    </div>
                    <div class="mb-3">
                        <label>Email</label>
                        <input type="email" name="email" class="form-control" value="{{ user.email }}" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Update Profile</button>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""")

write_file("templates/admin/users.html", """
{% extends 'base.html' %}
{% block content %}
<div class="d-flex justify-content-between align-items-center mb-4">
    <h3>Registered Users</h3>
    <a href="{{ url_for('admin.dashboard') }}" class="btn btn-outline-secondary">Back to Dashboard</a>
</div>
<div class="card shadow-sm">
    <div class="card-body">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th>User ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Role</th>
                    <th>Total Bookings</th>
                </tr>
            </thead>
            <tbody>
                {% for u in users %}
                <tr>
                    <td>{{ u.id }}</td>
                    <td>{{ u.name }}</td>
                    <td>{{ u.email }}</td>
                    <td>{{ u.role }}</td>
                    <td>{{ u.bookings|length }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
{% endblock %}
""")

write_file("templates/admin/bookings.html", """
{% extends 'base.html' %}
{% block content %}
<div class="d-flex justify-content-between align-items-center mb-4">
    <h3>All Bookings</h3>
    <a href="{{ url_for('admin.dashboard') }}" class="btn btn-outline-secondary">Back to Dashboard</a>
</div>
<div class="card shadow-sm">
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th>Booking ID</th>
                        <th>User ID</th>
                        <th>User Name</th>
                        <th>Route</th>
                        <th>Seats</th>
                        <th>Amount</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {% for b in bookings %}
                    <tr>
                        <td>{{ b.booking_reference }}</td>
                        <td>{{ b.user_id }}</td>
                        <td>{{ b.user.name }}</td>
                        <td>{{ b.bus.from_city }} &rarr; {{ b.bus.to_city }} <br><small class="text-muted">{{ b.journey_date }}</small></td>
                        <td>{{ b.seat_numbers }}</td>
                        <td>₹{{ b.total_amount }}</td>
                        <td>
                            <span class="badge {% if b.booking_status == 'Cancelled' %}bg-danger{% else %}bg-success{% endif %}">
                                {{ b.booking_status }}
                            </span>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>
{% endblock %}
""")

write_file("templates/admin/dashboard.html", """
{% extends 'base.html' %}
{% block content %}
<h3 class="mb-4">Admin Dashboard</h3>
<div class="row mb-4">
    <div class="col-md-3">
        <div class="card bg-primary text-white text-center shadow-sm" style="cursor: pointer;" onclick="window.location.href='{{ url_for('admin.users') }}'">
            <div class="card-body">
                <h4>Total Users</h4><h2>{{ users }}</h2>
                <small>View Users &rarr;</small>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card bg-success text-white text-center shadow-sm" style="cursor: pointer;" onclick="window.location.href='{{ url_for('admin.buses') }}'">
            <div class="card-body">
                <h4>Total Buses</h4><h2>{{ buses }}</h2>
                <small>View Buses &rarr;</small>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card bg-warning text-dark text-center shadow-sm" style="cursor: pointer;" onclick="window.location.href='{{ url_for('admin.bookings') }}'">
            <div class="card-body">
                <h4>Total Bookings</h4><h2>{{ bookings }}</h2>
                <small>View Bookings &rarr;</small>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card bg-info text-white text-center shadow-sm">
            <div class="card-body">
                <h4>Revenue</h4><h2>₹{{ revenue }}</h2>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""")

print("HTML updates applied.")
