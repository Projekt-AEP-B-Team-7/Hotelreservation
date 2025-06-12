from ui.booking_helper import calculate_vat_amounts

def get_seasonal_price(base_price: float, month: int) -> float:
    if month in [7, 8]:
        return base_price * 1.2
    elif month in [1, 2, 11]:
        return base_price * 0.85
    else:
        return base_price

def get_season_name(month: int) -> str:
    if month in [7, 8]:
        return "High Season (+20%)"
    elif month in [1, 2, 11]:
        return "Low Season (-15%)"
    else:
        return "Normal Season"

def display_pricing_period(check_in, check_out, num_nights, season):
    print(f"\nPeriod: {check_in.date()} to {check_out.date()} ({num_nights} nights) | Season: {season}")
    print("="*100)

def display_dynamic_pricing_for_room(room, facilities_manager, num_nights, month):
    room_facilities = facilities_manager.read_facilities_by_room(room)
    
    facilities_list = []
    if room_facilities:
        facilities_list = [facility.facility_name for facility in room_facilities]
    
    facilities_text = ", ".join(facilities_list) if facilities_list else "No facilities"
    
    season = get_season_name(month)
    
    # Preisberechnungen mit MwSt
    base_net_price = room.price_per_night
    seasonal_net_price = get_seasonal_price(base_net_price, month)
    total_net_price = seasonal_net_price * num_nights
    
    # MwSt-Berechnungen
    base_vat, base_gross = calculate_vat_amounts(base_net_price)
    seasonal_vat, seasonal_gross = calculate_vat_amounts(seasonal_net_price)
    total_vat, total_gross = calculate_vat_amounts(total_net_price)

    print(f"\nHotel: {room.hotel.name} | Room {room.room_number}")
    if room.hotel.address:
        print(f"Location: {room.hotel.address.city} | Stars: {room.hotel.stars}")
    print(f"Type: {room.room_type.description} | Max Guests: {room.room_type.max_guests}")
    print(f"Facilities: {facilities_text}")
    print()
    
    print("PRICING DETAILS:")
    print("-" * 50)
    
    # Base Price
    print(f"Base Price per night:")
    print(f"  Net: {base_net_price:.2f} CHF | VAT: {base_vat:.2f} CHF | Gross: {base_gross:.2f} CHF")
    
    # Seasonal Price
    print(f"Dynamic Price per night ({season}):")
    print(f"  Net: {seasonal_net_price:.2f} CHF | VAT: {seasonal_vat:.2f} CHF | Gross: {seasonal_gross:.2f} CHF")
    
    print()
    print(f"TOTAL FOR {num_nights} NIGHTS:")
    print("-" * 30)
    print(f"Net amount: {total_net_price:.2f} CHF")
    print(f"VAT (3.8%): {total_vat:.2f} CHF")
    print(f"TOTAL incl. VAT: {total_gross:.2f} CHF")
    print("=" * 80)

def display_all_dynamic_pricing(rooms, facilities_manager, num_nights, month):
    if not rooms:
        print("No rooms found.")
        return False
    
    try:
        for room in rooms:
            display_dynamic_pricing_for_room(room, facilities_manager, num_nights, month)
        return True
    except Exception as e:
        print(f"Error loading rooms: {e}")
        return False

def validate_pricing_search_again(search_again):
    if search_again in ['y', 'yes']:
        return True
    elif search_again in ['n', 'no']:
        print("Program ended.")
        return False
    else:
        print("Please enter 'y' for yes or 'n' for no.")
        return None