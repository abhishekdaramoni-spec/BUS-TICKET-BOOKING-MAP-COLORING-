import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

write_file("templates/buses.html", """
{% extends 'base.html' %}
{% block content %}
<div class="row mb-4">
    <div class="col-12">
        <h2 class="fw-bold" style="color: var(--primary);">{{ request.args.get('from') }} &rarr; {{ request.args.get('to') }}</h2>
        <p class="text-muted">{{ date }} | {{ passengers }} Passenger(s) | {{ buses|length }} buses available</p>
    </div>
</div>

<div class="row">
    <!-- Left Sidebar: Filters (UI only for demonstration) -->
    <div class="col-md-3 mb-4">
        <div class="card shadow-sm border-0" style="border-radius: 12px; position: sticky; top: 100px;">
            <div class="card-body">
                <h5 class="fw-bold mb-3 border-bottom pb-2">Filters</h5>
                
                <div class="mb-3">
                    <h6 class="fw-semibold small text-uppercase text-muted">Bus Type</h6>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" checked>
                        <label class="form-check-label">AC</label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" checked>
                        <label class="form-check-label">Non-AC</label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" checked>
                        <label class="form-check-label">Sleeper</label>
                    </div>
                </div>
                
                <div class="mb-3">
                    <h6 class="fw-semibold small text-uppercase text-muted">Price Range</h6>
                    <input type="range" class="form-range" min="0" max="2000">
                </div>
                
                <button class="btn btn-outline-primary w-100 btn-sm">Apply Filters</button>
            </div>
        </div>
    </div>
    
    <!-- Right Sidebar: Bus Cards -->
    <div class="col-md-9">
        {% for bus in buses %}
        <div class="card shadow-sm border-0 mb-4 bus-card" style="border-radius: 12px;">
            <div class="card-body p-4 d-flex flex-column flex-md-row justify-content-between align-items-center">
                <div class="mb-3 mb-md-0 w-100">
                    <div class="d-flex justify-content-between align-items-center mb-2">
                        <h4 class="fw-bold mb-0" style="color: var(--primary);">{{ bus.operator }}</h4>
                        <span class="badge" style="background-color: var(--accent); color: var(--primary); font-size: 0.9rem;">{{ bus.bus_type }}</span>
                    </div>
                    <div class="mb-2 text-warning fw-bold">★★★★★ {{ bus.rating }}</div>
                    
                    <div class="d-flex align-items-center gap-4 mt-3 mb-3">
                        <div class="text-center">
                            <h5 class="fw-bold mb-0">{{ bus.departure_time }}</h5>
                            <small class="text-muted text-uppercase">{{ bus.from_city }}</small>
                        </div>
                        <div class="text-muted d-flex align-items-center flex-column">
                            <small>{{ bus.duration }}</small>
                            <span>&rarr;</span>
                        </div>
                        <div class="text-center">
                            <h5 class="fw-bold mb-0">{{ bus.arrival_time }}</h5>
                            <small class="text-muted text-uppercase">{{ bus.to_city }}</small>
                        </div>
                    </div>
                    
                    <div>
                        <small class="text-muted fw-semibold">Amenities: </small>
                        <small class="text-muted">{{ bus.amenities }}</small>
                    </div>
                </div>
                
                <div class="text-md-end ms-md-4 mt-3 mt-md-0 border-start ps-md-4 w-100 text-center" style="max-width: 200px;">
                    <p class="text-muted small mb-1">Starting from</p>
                    <h3 class="text-primary fw-bold mb-3">₹{{ bus.base_price }}<span class="fs-6 fw-normal text-muted">/seat</span></h3>
                    <p class="text-success small mb-3">~20 seats available</p>
                    <a href="{{ url_for('booking.seats', bus_id=bus.id, date=date, passengers=passengers) }}" class="btn btn-primary w-100 fw-bold">SELECT SEAT</a>
                </div>
            </div>
        </div>
        {% else %}
        <div class="alert alert-warning shadow-sm border-0 rounded-3">No buses found for this route. Try changing the dates or locations.</div>
        {% endfor %}
    </div>
</div>
{% endblock %}
""")

write_file("templates/summary.html", """
{% extends 'base.html' %}
{% block content %}
<div class="row">
    <div class="col-md-8 mx-auto">
        <h3 class="mb-4 fw-bold text-primary">Booking Summary</h3>
        <div class="card shadow-lg border-0 mb-5" style="border-radius: 16px;">
            <div class="card-body p-5">
                <div class="d-flex justify-content-between align-items-center border-bottom pb-4 mb-4">
                    <div>
                        <h4 class="fw-bold mb-1" style="color: var(--primary);">{{ bus.operator }}</h4>
                        <span class="badge bg-secondary">{{ bus.bus_type }}</span>
                    </div>
                    <div class="text-end">
                        <h5 class="fw-bold mb-1">{{ bus.from_city }} &rarr; {{ bus.to_city }}</h5>
                        <p class="text-muted mb-0">{{ data.date }}</p>
                    </div>
                </div>
                
                <div class="row mb-4">
                    <div class="col-12">
                        <h6 class="text-uppercase text-muted fw-bold small mb-3">Passenger Information</h6>
                        <div class="table-responsive">
                            <table class="table table-sm">
                                <thead>
                                    <tr>
                                        <th>Name</th>
                                        <th>Gender</th>
                                        <th>Age</th>
                                        <th>Seat</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {% for p in data.passengers_info %}
                                    <tr>
                                        <td>{{ p.name }}</td>
                                        <td>{{ p.gender }}</td>
                                        <td>{{ p.age }}</td>
                                        <td class="fw-bold text-primary">{{ p.seat }}</td>
                                    </tr>
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
                
                <h6 class="text-uppercase text-muted fw-bold small mb-3">Fare Breakdown</h6>
                <div class="bg-light p-4 rounded-3 mb-4 border">
                    <div class="d-flex justify-content-between mb-2">
                        <span>Base Fare</span>
                        <span>₹{{ data.fare_details.base_fare }}</span>
                    </div>
                    <div class="d-flex justify-content-between mb-2">
                        <span>Bus Type Charge</span>
                        <span>₹{{ data.fare_details.bus_type_charge }}</span>
                    </div>
                    <div class="d-flex justify-content-between mb-2 pb-2 border-bottom">
                        <span>Weekend Surcharge</span>
                        <span>₹{{ data.fare_details.weekend_charge }}</span>
                    </div>
                    
                    <div class="d-flex justify-content-between mb-2 text-success pt-2">
                        <span>Group Discount</span>
                        <span>-₹{{ data.fare_details.group_discount }}</span>
                    </div>
                    <div class="d-flex justify-content-between mb-3 text-success pb-2 border-bottom">
                        <span>Early Booking Discount</span>
                        <span>-₹{{ data.fare_details.early_discount }}</span>
                    </div>
                    
                    <div class="d-flex justify-content-between pt-2">
                        <span class="fs-5 fw-bold text-dark">TOTAL</span>
                        <span class="fs-4 fw-bold text-primary">₹{{ data.fare_details.final_fare }}</span>
                    </div>
                </div>
                
                <form action="{{ url_for('booking.payment') }}" method="POST" id="payment-form">
                    <div class="mb-4">
                        <h6 class="text-uppercase text-muted fw-bold small mb-3">Simulated Payment Options</h6>
                        <select class="form-select form-select-lg mb-3">
                            <option>UPI</option>
                            <option>Credit Card</option>
                            <option>Debit Card</option>
                            <option>Net Banking</option>
                        </select>
                    </div>
                    
                    <button type="submit" class="btn btn-success w-100 btn-lg shadow fw-bold" id="pay-btn">PAY NOW</button>
                    
                    <div id="processing" class="text-center mt-3 d-none">
                        <div class="spinner-border text-success mb-2" role="status"></div>
                        <h5 class="text-success">Processing Payment...</h5>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<script>
    document.getElementById('payment-form').addEventListener('submit', function(e) {
        e.preventDefault();
        document.getElementById('pay-btn').classList.add('d-none');
        document.getElementById('processing').classList.remove('d-none');
        
        setTimeout(() => {
            document.getElementById('processing').innerHTML = '<h5 class="text-success fw-bold">✓ Payment Successful</h5>';
            setTimeout(() => {
                this.submit();
            }, 800);
        }, 1500);
    });
</script>
{% endblock %}
""")

print("Search and Summary UI updated.")
