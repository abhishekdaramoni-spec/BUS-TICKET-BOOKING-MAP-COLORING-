import os

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

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
                        <h5 class="text-muted mb-1">Booking Reference</h5>
                        <h4 class="text-primary">{{ booking.booking_reference }}</h4>
                    </div>
                    <div class="text-end">
                        <img src="https://api.qrserver.com/v1/create-qr-code/?size=100x100&data={{ booking.booking_reference }}" alt="QR Code">
                    </div>
                </div>
                
                <div class="row mb-3">
                    <div class="col-6"><p class="text-muted mb-0">Bus Operator</p><h5>{{ booking.bus.operator }}</h5></div>
                    <div class="col-6"><p class="text-muted mb-0">Bus Type</p><h5>{{ booking.bus.bus_type }}</h5></div>
                </div>
                <div class="row mb-3">
                    <div class="col-6"><p class="text-muted mb-0">From</p><h5>{{ booking.bus.from_city }}</h5></div>
                    <div class="col-6"><p class="text-muted mb-0">To</p><h5>{{ booking.bus.to_city }}</h5></div>
                </div>
                <div class="row mb-3">
                    <div class="col-6"><p class="text-muted mb-0">Journey Date</p><h5>{{ booking.journey_date }}</h5></div>
                    <div class="col-6"><p class="text-muted mb-0">Departure</p><h5>{{ booking.bus.departure_time }}</h5></div>
                </div>
                <div class="row mb-3">
                    <div class="col-6"><p class="text-muted mb-0">Seats</p><h5>{{ booking.seat_numbers }} ({{ booking.passenger_count }} pax)</h5></div>
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

write_file("templates/bookings.html", """
{% extends 'base.html' %}
{% block content %}
<h3 class="mb-4">My Bookings</h3>
<div class="row">
    {% for b in bookings %}
    <div class="col-md-12 mb-3">
        <div class="card shadow-sm border-start border-4 {% if b.booking_status == 'Cancelled' %}border-danger{% else %}border-success{% endif %}">
            <div class="card-body d-flex justify-content-between align-items-center">
                <div>
                    <h5 class="card-title">{{ b.booking_reference }} <span class="badge {% if b.booking_status == 'Cancelled' %}bg-danger{% else %}bg-success{% endif %}">{{ b.booking_status }}</span></h5>
                    <p class="mb-1 fw-bold">{{ b.bus.from_city }} &rarr; {{ b.bus.to_city }} on {{ b.journey_date }}</p>
                    <p class="text-muted small mb-0">{{ b.bus.operator }} | Seats: {{ b.seat_numbers }} | ₹{{ b.total_amount }}</p>
                </div>
                <div class="text-end">
                    {% if b.booking_status != 'Cancelled' %}
                        <a href="{{ url_for('booking.confirmation', booking_id=b.id) }}" class="btn btn-outline-primary btn-sm mb-1 d-block">View Ticket</a>
                        <form action="{{ url_for('booking.cancel', booking_id=b.id) }}" method="POST" onsubmit="return confirm('Are you sure you want to cancel this booking? Cancellation rules will apply.');">
                            <button type="submit" class="btn btn-outline-danger btn-sm w-100">Cancel Booking</button>
                        </form>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
    {% else %}
    <div class="alert alert-info">No bookings found.</div>
    {% endfor %}
</div>
{% endblock %}
""")

write_file("templates/graph_coloring.html", """
{% extends 'base.html' %}
{% block content %}
<div class="row">
    <div class="col-md-12">
        <h2 class="mb-3 text-primary">Bus Seat Allocation Using Graph Coloring</h2>
        <p class="lead">This project demonstrates a theoretical Graph-Coloring approach to bus seat allocation.</p>
    </div>
</div>

<div class="row mt-4">
    <div class="col-md-6">
        <div class="card shadow-sm h-100">
            <div class="card-header bg-dark text-white">Algorithm Explanation</div>
            <div class="card-body">
                <h5>Vertices & Edges</h5>
                <p>Every bus seat is a <strong>Vertex</strong>. If two seats are adjacent physically (horizontally or vertically), an <strong>Edge</strong> connects them.</p>
                
                <h5>Coloring Rule</h5>
                <p>Two connected (conflicting) seats must <em>not</em> receive the same color. The colors represent distinct <strong>Allocation Groups</strong>.</p>
                
                <pre class="bg-light p-3 rounded border">
def greedy_coloring(graph):
    colors = {}
    for vertex in graph:
        used = {colors[n] for n in graph[vertex] 
                if n in colors}
        c = 0
        while c in used: c += 1
        colors[vertex] = c
    return colors
                </pre>
            </div>
        </div>
    </div>
    <div class="col-md-6">
        <div class="card shadow-sm h-100">
            <div class="card-header bg-dark text-white">Algorithm Flow</div>
            <div class="card-body text-center">
                <div class="d-inline-block text-start p-3 bg-light border rounded">
                    CREATE SEAT VERTICES<br>
                    &darr;<br>
                    CREATE CONFLICT EDGES<br>
                    &darr;<br>
                    CHOOSE FIRST SEAT<br>
                    &darr;<br>
                    CHECK NEIGHBOUR COLORS<br>
                    &darr;<br>
                    ASSIGN LOWEST AVAILABLE COLOR<br>
                    &darr;<br>
                    GENERATE COLORING &amp; DISPLAY
                </div>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-md-12">
        <div class="card shadow-sm">
            <div class="card-body text-center">
                <h4 class="mb-4">Example Visual ({{ bus.operator if bus else 'Demo' }})</h4>
                <div class="d-flex justify-content-center mb-3">
                    <span class="badge me-2" style="background-color: var(--color-0); color: black;">Color 0 (Group A)</span>
                    <span class="badge me-2" style="background-color: var(--color-1); color: black;">Color 1 (Group B)</span>
                    <span class="badge me-2" style="background-color: var(--color-2); color: black;">Color 2 (Group C)</span>
                    <span class="badge me-2" style="background-color: var(--color-3); color: black;">Color 3 (Group D)</span>
                </div>
                <div class="seat-grid d-flex flex-wrap justify-content-center mx-auto" style="width: 300px;">
                    {% for seat in seats %}
                        {% set g_color = 'color-' ~ seat.graph_color %}
                        <div class="seat-wrapper mb-3" style="width: 20%;">
                            <div class="btn disabled" style="background-color: var(--{{ g_color }}); width: 80%; height: 40px; border: 1px solid #333;">
                                {{ seat.seat_number }}
                            </div>
                            <small class="d-block" style="font-size: 0.65rem;">C:{{ seat.graph_color }}</small>
                        </div>
                    {% endfor %}
                </div>
                <div class="mt-4 border-top pt-3">
                    <p class="text-muted">Complexity: <strong>O(V + E)</strong> where V = vertices (seats) and E = edges (adjacencies).</p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""")

write_file("static/css/style.css", """
:root {
    --color-0: #ffb3ba;
    --color-1: #ffdfba;
    --color-2: #ffffba;
    --color-3: #baffc9;
    --color-4: #bae1ff;
    --color-5: #e8baff;
}

body {
    background-color: #f8f9fa;
}

.hero-section {
    background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
}
""")

write_file("templates/login.html", """
{% extends 'base.html' %}
{% block content %}
<div class="row mt-5">
    <div class="col-md-4 mx-auto">
        <h3 class="text-center mb-4">Login</h3>
        <div class="card shadow-sm">
            <div class="card-body">
                <form method="POST">
                    <div class="mb-3">
                        <label>Email</label>
                        <input type="email" name="email" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label>Password</label>
                        <input type="password" name="password" class="form-control" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Login</button>
                </form>
                <p class="mt-3 text-center"><small>Don't have an account? <a href="{{ url_for('auth.register') }}">Register</a></small></p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""")

write_file("templates/register.html", """
{% extends 'base.html' %}
{% block content %}
<div class="row mt-5">
    <div class="col-md-4 mx-auto">
        <h3 class="text-center mb-4">Register</h3>
        <div class="card shadow-sm">
            <div class="card-body">
                <form method="POST">
                    <div class="mb-3">
                        <label>Name</label>
                        <input type="text" name="name" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label>Email</label>
                        <input type="email" name="email" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label>Password</label>
                        <input type="password" name="password" class="form-control" required>
                    </div>
                    <button type="submit" class="btn btn-success w-100">Register</button>
                </form>
            </div>
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
        <div class="card bg-primary text-white text-center shadow-sm">
            <div class="card-body">
                <h4>Total Users</h4><h2>{{ users }}</h2>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card bg-success text-white text-center shadow-sm">
            <div class="card-body">
                <h4>Total Buses</h4><h2>{{ buses }}</h2>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card bg-warning text-white text-center shadow-sm">
            <div class="card-body">
                <h4>Bookings</h4><h2>{{ bookings }}</h2>
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
print("HTML bootstrap 3 complete.")
