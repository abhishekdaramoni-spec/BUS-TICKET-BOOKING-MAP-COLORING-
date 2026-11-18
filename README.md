# BusGo — Bus Ticket Booking System

## Description
A full-stack Bus Ticket Booking Website built with Python and Flask. The primary academic feature of this project is the implementation of a **Web/Graph Colouring Algorithm** for bus seat allocation, where seats are modeled as graph vertices and physical adjacencies as edges.

## Features
- **Graph Coloring Algorithm**: Uses a Greedy Graph Coloring approach to assign non-conflicting colors to adjacent bus seats, representing allocation groups.
- **Rule-Based Business Engine**: Calculates fares with dynamic surcharges (AC, Sleeper, Weekends) and discounts (Group, Early Booking).
- **Cancellation Engine**: Determines refund eligibility based on the time remaining before the journey.
- **Full-Stack Application**: Includes authentication, bus searching, interactive seat selection, mock payment, and a digital ticket generator.
- **Admin Dashboard**: For monitoring buses, users, bookings, and revenue.

## Technology Stack
- **Backend**: Python 3, Flask, Jinja2
- **Database**: SQLite, Flask-SQLAlchemy
- **Frontend**: HTML5, CSS3, Vanilla JS, Bootstrap 5

## Project Structure
- `algorithms/`: Core graph coloring and rule-based algorithms.
- `models/`: Database models (User, Bus, Seat, Booking).
- `routes/`: Flask blueprints for main site, auth, booking, and admin.
- `templates/`: Jinja HTML views.
- `static/`: Custom CSS and JavaScript.

## How the Rule-Based Algorithm Works
1. **Graph Creation**: `algorithms/graph_coloring.py` iterates over the bus layout, generating an adjacency list.
2. **Color Assignment**: A Greedy algorithm ensures no two physically adjacent seats share the same allocation group color.
3. **Seat Allocation**: The colors are presented visually on the frontend to the user as they select seats, ensuring groups are clustered intelligently according to the algorithm's output.

## Installation Steps
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - Windows: `venv\\Scripts\\activate`
   - Mac/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Seed the database with demo data:
   ```bash
   python seed.py
   ```

## How to Run
Start the Flask development server:
```bash
python app.py
```
Visit `http://localhost:5000` in your web browser.

## Demo Credentials
- **Admin**: `admin@busgo.com` / `Admin@123`
- **User 1 (Rahul)**: `rahul@example.com` / `Rahul@123`
- **User 2 (Priya)**: `priya@example.com` / `Priya@123`
- **User 3 (Amit)**: `amit@example.com` / `Amit@123`

## Test Cases
Tests are implemented in the `tests/` directory. Run them using pytest:
```bash
python -m pytest tests/test_graph_coloring.py
```
Test scenarios include two connected vertices, bipartite graphs, disconnected components, and realistic bus layout adjacency.
