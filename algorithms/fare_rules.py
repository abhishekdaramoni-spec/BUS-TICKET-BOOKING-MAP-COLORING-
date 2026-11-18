from datetime import datetime

def calculate_base_fare(base_price, passengers):
    return base_price * passengers

def calculate_bus_type_charge(bus_type, passengers):
    if bus_type == "AC":
        return 100 * passengers
    elif bus_type == "Sleeper":
        return 150 * passengers
    elif bus_type == "AC Sleeper":
        return 200 * passengers
    return 0

def calculate_weekend_charge(journey_date_str, current_total):
    # journey_date_str in format YYYY-MM-DD
    try:
        j_date = datetime.strptime(journey_date_str, "%Y-%m-%d")
        # 5 is Saturday, 6 is Sunday
        if j_date.weekday() >= 5:
            return current_total * 0.05
    except ValueError:
        pass
    return 0
