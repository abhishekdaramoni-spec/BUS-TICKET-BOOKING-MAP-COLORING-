import os
from app import create_app
from models import db, User, Bus, Seat, Booking
from werkzeug.security import generate_password_hash
from algorithms.graph_coloring import create_seat_graph, greedy_coloring

def seed_database():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        # 1. Create Users
        admin = User(name="Admin", email="admin@busgo.com", password_hash=generate_password_hash("Admin@123"), role="admin")
        rahul = User(name="Rahul Patel", email="rahul@example.com", password_hash=generate_password_hash("Rahul@123"), role="user")
        priya = User(name="Priya Shah", email="priya@example.com", password_hash=generate_password_hash("Priya@123"), role="user")
        amit = User(name="Amit Mehta", email="amit@example.com", password_hash=generate_password_hash("Amit@123"), role="user")
        db.session.add_all([admin, rahul, priya, amit])
        
        # 2. Create Buses
        buses_data = [
            {"op": "Patel Travels", "from": "Ahmedabad", "to": "Rajkot", "dep": "06:30 AM", "arr": "10:30 AM", "dur": "4h 0m", "type": "AC Sleeper", "price": 500, "rating": 4.5, "amenities": "WiFi, Water"},
            {"op": "Eagle Express", "from": "Ahmedabad", "to": "Surat", "dep": "08:00 AM", "arr": "12:30 PM", "dur": "4h 30m", "type": "AC", "price": 400, "rating": 4.2, "amenities": "Water, Charging"},
            {"op": "Neeta Tours", "from": "Ahmedabad", "to": "Vadodara", "dep": "09:00 AM", "arr": "11:00 AM", "dur": "2h 0m", "type": "Non-AC", "price": 200, "rating": 3.8, "amenities": "None"},
            {"op": "Saurashtra Express", "from": "Rajkot", "to": "Ahmedabad", "dep": "14:00 PM", "arr": "18:00 PM", "dur": "4h 0m", "type": "Sleeper", "price": 450, "rating": 4.0, "amenities": "Charging"},
            {"op": "Mahasagar Travels", "from": "Surat", "to": "Mumbai", "dep": "22:00 PM", "arr": "06:00 AM", "dur": "8h 0m", "type": "AC Sleeper", "price": 800, "rating": 4.7, "amenities": "WiFi, Water, Blanket"},
            {"op": "Patel Travels", "from": "Ahmedabad", "to": "Rajkot", "dep": "18:30 PM", "arr": "22:30 PM", "dur": "4h 0m", "type": "AC", "price": 400, "rating": 4.3, "amenities": "Water"},
            {"op": "Eagle Express", "from": "Ahmedabad", "to": "Surat", "dep": "13:00 PM", "arr": "17:30 PM", "dur": "4h 30m", "type": "Sleeper", "price": 450, "rating": 4.1, "amenities": "Charging"},
            {"op": "Neeta Tours", "from": "Ahmedabad", "to": "Vadodara", "dep": "15:00 PM", "arr": "17:00 PM", "dur": "2h 0m", "type": "AC Sleeper", "price": 300, "rating": 4.4, "amenities": "Water, Charging"},
            {"op": "Saurashtra Express", "from": "Rajkot", "to": "Ahmedabad", "dep": "06:00 AM", "arr": "10:00 AM", "dur": "4h 0m", "type": "AC", "price": 500, "rating": 4.2, "amenities": "WiFi"},
            {"op": "Mahasagar Travels", "from": "Surat", "to": "Mumbai", "dep": "20:00 PM", "arr": "04:00 AM", "dur": "8h 0m", "type": "Sleeper", "price": 700, "rating": 4.5, "amenities": "Blanket"},
        ]
        
        bus_objects = []
        for b in buses_data:
            bus = Bus(
                operator=b["op"], from_city=b["from"], to_city=b["to"],
                departure_time=b["dep"], arrival_time=b["arr"], duration=b["dur"],
                bus_type=b["type"], base_price=b["price"], rating=b["rating"],
                amenities=b["amenities"]
            )
            db.session.add(bus)
            bus_objects.append(bus)
        
        db.session.commit()
        
        # 3. Create Seats and Graph Coloring
        rows = ['A', 'B', 'C', 'D', 'E']
        cols = ['1', '2', '3', '4']
        
        for bus in bus_objects:
            seats_for_bus = []
            for r in rows:
                for c in cols:
                    seat_num = f"{r}{c}"
                    status = "available"
                    # Make some seats booked randomly or deterministically
                    if r == 'A' and c in ['1', '2']:
                        status = "booked"
                    seat = Seat(bus_id=bus.id, seat_number=seat_num, seat_type="Standard", price=bus.base_price, status=status)
                    seats_for_bus.append(seat)
            
            # Apply Graph Coloring
            graph = create_seat_graph(seats_for_bus)
            colors = greedy_coloring(graph)
            
            for seat in seats_for_bus:
                seat.graph_color = colors.get(seat.seat_number, 0)
                db.session.add(seat)
                
        db.session.commit()
        print("Database seeded successfully with Users, Buses, Seats, and Graph Colors.")

if __name__ == '__main__':
    seed_database()
