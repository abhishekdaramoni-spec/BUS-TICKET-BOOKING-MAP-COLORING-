import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

write_file("templates/ticket.html", """
{% extends 'base.html' %}
{% block content %}
<div class="row">
    <div class="col-md-8 mx-auto">
        <div class="card shadow border-0 mb-4" style="border-radius: 16px; overflow: hidden;">
            <div class="card-header text-white text-center py-4" style="background-color: var(--primary);">
                <h3 class="mb-0 fw-bold">BUSGO</h3>
                <p class="text-accent mb-0">✓ BOOKING CONFIRMED</p>
            </div>
            <div class="card-body p-5">
                <div class="d-flex justify-content-between mb-4 pb-4 border-bottom">
                    <div>
                        <h6 class="text-muted text-uppercase tracking-wide mb-1">Booking ID</h6>
                        <h3 class="text-primary fw-bold">{{ booking.booking_reference }}</h3>
                    </div>
                    <div class="text-end">
                        <img src="https://api.qrserver.com/v1/create-qr-code/?size=100x100&data={{ booking.booking_reference }}" alt="QR Code" class="shadow-sm rounded">
                    </div>
                </div>
                
                <div class="row mb-4 pb-4 border-bottom">
                    <div class="col-md-4 mb-3 mb-md-0"><p class="text-muted mb-1 text-uppercase small">User ID</p><h5 class="fw-semibold">{{ booking.user.id }}</h5></div>
                    <div class="col-md-4 mb-3 mb-md-0"><p class="text-muted mb-1 text-uppercase small">Account Name</p><h5 class="fw-semibold">{{ booking.user.name }}</h5></div>
                    <div class="col-md-4"><p class="text-muted mb-1 text-uppercase small">Account Email</p><h5 class="fw-semibold">{{ booking.user.email }}</h5></div>
                </div>

                <div class="row mb-4">
                    <div class="col-6 mb-4"><p class="text-muted mb-1 text-uppercase small">Bus Operator</p><h5 class="fw-semibold">{{ booking.bus.operator }}</h5></div>
                    <div class="col-6 mb-4"><p class="text-muted mb-1 text-uppercase small">Route</p><h5 class="fw-semibold">{{ booking.bus.from_city }} &rarr; {{ booking.bus.to_city }}</h5></div>
                    
                    <div class="col-6 mb-4"><p class="text-muted mb-1 text-uppercase small">Journey Date</p><h5 class="fw-semibold">{{ booking.journey_date }}</h5></div>
                    <div class="col-6 mb-4"><p class="text-muted mb-1 text-uppercase small">Departure</p><h5 class="fw-semibold">{{ booking.bus.departure_time }}</h5></div>
                    
                    <div class="col-6 mb-4">
                        <p class="text-muted mb-1 text-uppercase small">Passengers & Seats</p>
                        {% for p in booking.passengers_list %}
                            <h6 class="mb-1 fw-semibold">{{ p.name }} (Seat {{ p.seat_number }})</h6>
                        {% else %}
                            <h6 class="fw-semibold">{{ booking.seat_numbers }}</h6>
                        {% endfor %}
                    </div>
                    
                    <div class="col-6 mb-4">
                        <p class="text-muted mb-1 text-uppercase small">Total Paid</p>
                        <h4 class="text-success fw-bold">₹{{ booking.total_amount }}</h4>
                        <span class="badge bg-success">{{ booking.payment_status }}</span>
                    </div>
                </div>
                
                <div class="text-center mt-4 d-flex justify-content-center gap-3">
                    <button class="btn btn-outline-dark px-4 py-2 fw-semibold" onclick="window.print()">PRINT TICKET</button>
                    <a href="{{ url_for('booking.my_bookings') }}" class="btn btn-primary px-4 py-2 fw-semibold">MY BOOKINGS</a>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""")

write_file("templates/graph_coloring.html", """
{% extends 'base.html' %}
{% block content %}
<div class="row mb-5">
    <div class="col-md-10 mx-auto text-center">
        <span class="text-uppercase tracking-wide text-info fw-bold mb-2 d-block" style="letter-spacing: 2px; color: var(--accent) !important;">Academic Algorithm</span>
        <h1 class="mb-3 fw-bold" style="color: var(--primary);">Smart Seat Allocation Using Graph Coloring</h1>
        <p class="lead text-muted">A theoretical implementation of the Greedy Graph Coloring algorithm to logically group seats based on conflict avoidance.</p>
    </div>
</div>

<div class="row mt-4 g-4">
    <div class="col-md-6">
        <div class="card shadow h-100 border-0" style="border-radius: 12px;">
            <div class="card-header bg-white border-bottom py-3">
                <h5 class="mb-0 fw-bold" style="color: var(--primary);">Algorithm Concepts</h5>
            </div>
            <div class="card-body p-4">
                <div class="mb-4">
                    <h6 class="text-uppercase text-muted fw-bold small mb-2">Problem</h6>
                    <p>Efficiently organize and visualize seat relationships to prevent conflicting allocations (e.g., social distancing, distinct grouping logic).</p>
                </div>
                <div class="mb-4">
                    <h6 class="text-uppercase text-muted fw-bold small mb-2">Representation</h6>
                    <ul class="list-unstyled">
                        <li class="mb-2"><strong>Vertex:</strong> A single bus seat.</li>
                        <li class="mb-2"><strong>Edge:</strong> Relationship/conflict between physically adjacent seats.</li>
                        <li class="mb-2"><strong>Color:</strong> The resulting Allocation Group (Group A, B, C...).</li>
                    </ul>
                </div>
                <div class="mb-4">
                    <h6 class="text-uppercase text-muted fw-bold small mb-2">Rule</h6>
                    <div class="p-3 bg-light rounded border border-warning">
                        <em>"If Seat A1 is connected to Seat A2, A1 and A2 must have different colors."</em>
                    </div>
                </div>
                <div>
                    <h6 class="text-uppercase text-muted fw-bold small mb-2">Complexity</h6>
                    <p class="mb-0"><strong>Time & Space: O(V + E)</strong> where V = number of seats, E = number of connections.</p>
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-md-6">
        <div class="card shadow h-100 border-0" style="border-radius: 12px;">
            <div class="card-header bg-white border-bottom py-3">
                <h5 class="mb-0 fw-bold" style="color: var(--primary);">Greedy Graph Coloring Logic</h5>
            </div>
            <div class="card-body p-4">
                <pre class="bg-dark text-light p-4 rounded" style="font-size: 0.9rem; overflow-x: auto;">
def greedy_coloring(graph):
    colors = {}
    for vertex in graph:
        used_colors = {
            colors[n] 
            for n in graph[vertex] 
            if n in colors
        }
        
        color = 0
        while color in used_colors:
            color += 1
            
        colors[vertex] = color
    return colors
                </pre>
                
                <div class="mt-4" id="animation-container">
                    <h6 class="fw-bold mb-3">Animation Steps:</h6>
                    <div id="anim-step" class="alert alert-info py-2">Click 'Start Animation' to view the flow.</div>
                    <button class="btn btn-accent w-100 fw-bold" id="start-anim">▶ Start Animation</button>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="row mt-5">
    <div class="col-md-12">
        <div class="card shadow border-0" style="border-radius: 12px;">
            <div class="card-body text-center p-5">
                <h4 class="mb-4 fw-bold" style="color: var(--primary);">Real-world Application ({{ bus.operator if bus else 'Demo Layout' }})</h4>
                
                <div class="d-flex justify-content-center mb-4 gap-3 flex-wrap">
                    <span class="badge py-2 px-3 shadow-sm text-dark" style="background-color: var(--color-0);">Color 0 (Group A)</span>
                    <span class="badge py-2 px-3 shadow-sm text-dark" style="background-color: var(--color-1);">Color 1 (Group B)</span>
                    <span class="badge py-2 px-3 shadow-sm text-dark" style="background-color: var(--color-2);">Color 2 (Group C)</span>
                    <span class="badge py-2 px-3 shadow-sm text-dark" style="background-color: var(--color-3);">Color 3 (Group D)</span>
                </div>
                
                <div class="seat-grid d-flex flex-wrap justify-content-center mx-auto" style="width: 320px; background: #f8fafc; padding: 2rem; border-radius: 12px; border: 1px solid #e2e8f0;">
                    {% for seat in seats %}
                        {% set g_color = 'color-' ~ seat.graph_color %}
                        <div class="seat-wrapper mb-3" style="width: 25%;">
                            <div class="btn disabled fw-bold shadow-sm" style="background-color: var(--{{ g_color }}); width: 80%; height: 45px; border: 1px solid rgba(0,0,0,0.1); color: #334155;">
                                {{ seat.seat_number }}
                            </div>
                            <small class="d-block mt-1 fw-semibold text-muted" style="font-size: 0.7rem;">Group {{ seat.graph_color }}</small>
                        </div>
                    {% endfor %}
                </div>
                
                <div class="mt-4 pt-3 d-flex justify-content-around text-muted">
                    <div><strong>Vertices:</strong> {{ seats|length }}</div>
                    <div><strong>Edges:</strong> {{ (seats|length * 2) - 10 }} (Approx)</div>
                    <div><strong>Colors Used:</strong> 4</div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    document.getElementById('start-anim').addEventListener('click', function() {
        const steps = [
            "Step 1: Select Vertex A1",
            "Step 2: Check neighboring seats (A2, B1)",
            "Step 3: Find used colors (None currently)",
            "Step 4: Assign smallest available color (Color 0) to A1",
            "Step 5: Move to Vertex A2",
            "Step 6: Check neighbors (A1 is Color 0)",
            "Step 7: Assign smallest available color (Color 1) to A2",
            "Step 8: Repeat for all seats..."
        ];
        let i = 0;
        const box = document.getElementById('anim-step');
        this.disabled = true;
        
        const interval = setInterval(() => {
            box.innerText = steps[i];
            i++;
            if(i >= steps.length) {
                clearInterval(interval);
                this.disabled = false;
                this.innerText = "↻ Replay Animation";
            }
        }, 1500);
    });
</script>
{% endblock %}
""")

print("Ticket and Graph Coloring UI updated.")
