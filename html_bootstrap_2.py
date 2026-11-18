import os

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

write_file("templates/seats.html", """
{% extends 'base.html' %}
{% block content %}
<div class="row">
    <div class="col-md-7">
        <h3>Select Seats</h3>
        <p class="text-muted">Graph Coloring Algorithm dynamically allocates seat colors to prevent adjacent selection conflicts if needed. Colors represent allocation groups.</p>
        
        <div class="d-flex mb-3 align-items-center">
            <span class="me-3"><strong>Graph Groups:</strong></span>
            <span class="badge me-2" style="background-color: var(--color-0); color: black;">Group 0</span>
            <span class="badge me-2" style="background-color: var(--color-1); color: black;">Group 1</span>
            <span class="badge me-2" style="background-color: var(--color-2); color: black;">Group 2</span>
            <span class="badge me-2" style="background-color: var(--color-3); color: black;">Group 3</span>
        </div>
        <div class="d-flex mb-4 align-items-center">
            <span class="me-3"><strong>Status:</strong></span>
            <span class="badge bg-secondary me-2">Available</span>
            <span class="badge bg-danger me-2">Booked</span>
            <span class="badge bg-primary">Selected</span>
        </div>
        
        <div class="bus-layout bg-light p-4 rounded text-center shadow-sm" style="max-width: 400px; margin: 0 auto;">
            <div class="driver-seat mb-4 text-end pe-4 fw-bold">DRIVER</div>
            <div class="seat-grid d-flex flex-wrap justify-content-between" style="width: 300px; margin: 0 auto;">
                {% for seat in seats %}
                <div class="seat-wrapper mb-3" style="width: 20%;">
                    {% set g_color = 'color-' ~ seat.graph_color %}
                    <button class="seat-btn btn 
                        {% if seat.status == 'booked' %}btn-danger disabled
                        {% else %}btn-outline-dark{% endif %}"
                        data-seat="{{ seat.seat_number }}"
                        data-color="{{ seat.graph_color }}"
                        data-status="{{ seat.status }}"
                        style="{% if seat.status == 'available' %}background-color: var(--{{ g_color }});{% endif %} width: 100%; height: 50px;">
                        {{ seat.seat_number }}
                    </button>
                    <small class="d-block" style="font-size: 0.6rem;">G: {{ seat.graph_color }}</small>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
    <div class="col-md-5">
        <div class="card shadow-sm mt-5">
            <div class="card-body">
                <h4>Booking Details</h4>
                <p><strong>Bus:</strong> {{ bus.operator }} ({{ bus.bus_type }})</p>
                <p><strong>Passengers:</strong> <span id="passenger-count">{{ passengers }}</span></p>
                <p><strong>Selected:</strong> <span id="selected-list">None</span></p>
                
                <form action="{{ url_for('booking.passenger') }}" method="POST" id="seat-form">
                    <input type="hidden" name="bus_id" value="{{ bus.id }}">
                    <input type="hidden" name="date" value="{{ date }}">
                    <input type="hidden" name="passengers" id="passengers-input" value="{{ passengers }}">
                    <input type="hidden" name="selected_seats" id="selected-seats-input">
                    <button type="submit" class="btn btn-primary w-100 mt-3" id="continue-btn" disabled>Continue</button>
                </form>
            </div>
        </div>
    </div>
</div>

<script>
    const maxPassengers = parseInt(document.getElementById('passenger-count').innerText);
    let selectedSeats = [];

    document.querySelectorAll('.seat-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            if (this.dataset.status === 'booked') return;

            const seatNum = this.dataset.seat;
            const originalColorVar = '--color-' + this.dataset.color;
            
            if (selectedSeats.includes(seatNum)) {
                // Deselect
                selectedSeats = selectedSeats.filter(s => s !== seatNum);
                this.classList.remove('btn-primary', 'text-white');
                this.style.backgroundColor = `var(${originalColorVar})`;
            } else {
                // Select
                if (selectedSeats.length >= maxPassengers) {
                    alert('You have already selected the maximum number of seats for this booking.');
                    return;
                }
                selectedSeats.push(seatNum);
                this.classList.add('btn-primary', 'text-white');
                this.style.backgroundColor = ''; // remove inline to let class take over
            }
            
            document.getElementById('selected-list').innerText = selectedSeats.length > 0 ? selectedSeats.join(', ') : 'None';
            document.getElementById('selected-seats-input').value = selectedSeats.join(',');
            document.getElementById('continue-btn').disabled = selectedSeats.length !== maxPassengers;
        });
    });
</script>
{% endblock %}
""")

write_file("templates/passenger.html", """
{% extends 'base.html' %}
{% block content %}
<div class="row">
    <div class="col-md-8 mx-auto">
        <h3 class="mb-4">Passenger Details</h3>
        <div class="card shadow-sm mb-4">
            <div class="card-body">
                <form action="{{ url_for('booking.summary') }}" method="POST">
                    <div class="mb-3">
                        <label>Full Name</label>
                        <input type="text" class="form-control" name="full_name" required>
                    </div>
                    <div class="mb-3">
                        <label>Age</label>
                        <input type="number" class="form-control" name="age" required>
                    </div>
                    <div class="mb-3">
                        <label>Gender</label>
                        <select class="form-select" name="gender">
                            <option>Male</option><option>Female</option><option>Other</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label>Phone</label>
                        <input type="text" class="form-control" name="phone" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Review Booking Summary</button>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""")

write_file("templates/summary.html", """
{% extends 'base.html' %}
{% block content %}
<div class="row">
    <div class="col-md-8 mx-auto">
        <h3 class="mb-4">Booking Summary</h3>
        <div class="card shadow-sm">
            <div class="card-body">
                <h5 class="card-title">{{ bus.operator }} - {{ bus.bus_type }}</h5>
                <p>{{ bus.from_city }} to {{ bus.to_city }}</p>
                <hr>
                <div class="row">
                    <div class="col-6"><p><strong>Date:</strong> {{ data.date }}</p></div>
                    <div class="col-6"><p><strong>Time:</strong> {{ bus.departure_time }}</p></div>
                    <div class="col-6"><p><strong>Passengers:</strong> {{ data.passengers }}</p></div>
                    <div class="col-6"><p><strong>Seats:</strong> {{ data.selected_seats }}</p></div>
                </div>
                
                <h5 class="mt-4">Fare Breakdown</h5>
                <table class="table table-bordered mt-2">
                    <tbody>
                        <tr><td>Base Fare</td><td class="text-end">₹{{ data.fare_details.base_fare }}</td></tr>
                        <tr><td>Bus Type Surcharge</td><td class="text-end">₹{{ data.fare_details.bus_type_charge }}</td></tr>
                        <tr><td>Weekend Surcharge</td><td class="text-end">₹{{ data.fare_details.weekend_charge }}</td></tr>
                        <tr class="text-success"><td>Group Discount</td><td class="text-end">-₹{{ data.fare_details.group_discount }}</td></tr>
                        <tr class="text-success"><td>Early Booking Discount</td><td class="text-end">-₹{{ data.fare_details.early_discount }}</td></tr>
                        <tr class="fw-bold fs-5"><td>Final Fare</td><td class="text-end text-primary">₹{{ data.fare_details.final_fare }}</td></tr>
                    </tbody>
                </table>
                
                <form action="{{ url_for('booking.payment') }}" method="POST">
                    <button type="submit" class="btn btn-success w-100 btn-lg mt-3">Proceed to Mock Payment</button>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""")
print("HTML bootstrap 2 complete.")
