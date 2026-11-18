from datetime import datetime

def calculate_refund(journey_date_str, journey_time_str, total_amount):
    try:
        # e.g., journey_date_str = "2026-09-15", journey_time_str = "06:30 AM"
        # Parse combined date and time
        j_datetime_str = f"{journey_date_str} {journey_time_str}"
        j_date = datetime.strptime(j_datetime_str, "%Y-%m-%d %I:%M %p")
        now = datetime.now()
        
        if now >= j_date:
            return {
                "cancellation_allowed": False,
                "refund_percentage": 0,
                "refund_amount": 0,
                "message": "Journey has already started or passed. Cancellation not allowed."
            }
            
        time_difference = j_date - now
        hours_until_journey = time_difference.total_seconds() / 3600
        
        if hours_until_journey > 24:
            return {
                "cancellation_allowed": True,
                "refund_percentage": 80,
                "refund_amount": round(total_amount * 0.80, 2),
                "message": "Cancellation successful. 80% refund initiated."
            }
        elif 12 <= hours_until_journey <= 24:
            return {
                "cancellation_allowed": True,
                "refund_percentage": 50,
                "refund_amount": round(total_amount * 0.50, 2),
                "message": "Cancellation successful. 50% refund initiated."
            }
        else:
            return {
                "cancellation_allowed": True,
                "refund_percentage": 0,
                "refund_amount": 0,
                "message": "Cancellation successful. No refund for cancellations within 12 hours."
            }
    except Exception as e:
        return {
            "cancellation_allowed": False,
            "refund_percentage": 0,
            "refund_amount": 0,
            "message": f"Error calculating refund: {str(e)}"
        }
