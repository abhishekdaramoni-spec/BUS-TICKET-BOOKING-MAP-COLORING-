from datetime import datetime
from .fare_rules import calculate_bus_type_charge, calculate_weekend_charge

def calculate_group_discount(passenger_count, total_amount):
    if passenger_count >= 4:
        return total_amount * 0.10
    return 0

def calculate_early_booking_discount(journey_date_str, total_amount):
    try:
        j_date = datetime.strptime(journey_date_str, "%Y-%m-%d")
        now = datetime.now()
        days_until_journey = (j_date - now).days
        if days_until_journey > 15:
            return total_amount * 0.05
    except ValueError:
        pass
    return 0

def calculate_final_fare(base_price, passengers, bus_type, journey_date_str):
    base_fare = base_price * passengers
    bus_type_charge = calculate_bus_type_charge(bus_type, passengers)
    
    subtotal1 = base_fare + bus_type_charge
    weekend_charge = calculate_weekend_charge(journey_date_str, subtotal1)
    
    subtotal2 = subtotal1 + weekend_charge
    
    group_discount = calculate_group_discount(passengers, subtotal2)
    early_discount = calculate_early_booking_discount(journey_date_str, subtotal2)
    
    final_fare = subtotal2 - group_discount - early_discount
    
    return {
        "base_fare": round(base_fare, 2),
        "bus_type_charge": round(bus_type_charge, 2),
        "weekend_charge": round(weekend_charge, 2),
        "group_discount": round(group_discount, 2),
        "early_discount": round(early_discount, 2),
        "final_fare": round(final_fare, 2)
    }

