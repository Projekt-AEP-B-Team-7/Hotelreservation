def filter_suitable_rooms(available_rooms, input_guest):
    suitable_rooms = []
    for room in available_rooms:
        if room.room_type and room.room_type.max_guests >= input_guest:
            suitable_rooms.append(room)
    return suitable_rooms

def display_available_rooms_details(hotels, room_manager, facilities_manager, input_city, checkin, checkout, input_guest, num_nights):
    if not hotels:
        print(f"No hotels found in '{input_city}'.")
        return

    print(f"\nAvailable rooms in {input_city} from {checkin} to {checkout} for {input_guest} guest(s) ({num_nights} nights):")
    
    rooms_found = False

    for hotel in hotels:
        available_rooms = room_manager.read_available_rooms_by_hotel(hotel, checkin, checkout)
        suitable_rooms = filter_suitable_rooms(available_rooms, input_guest)
        
        if suitable_rooms:
            rooms_found = True
            a = hotel.address
            print(f"\nHotel: {hotel.name} | Stars: {hotel.stars} | Street: {a.street} | City: {a.city} | ZIP: {a.zip_code}")
            
            for room in suitable_rooms:
                rt = room.room_type
                total_price = room.price_per_night * num_nights
                
                print(f"  Room {room.room_number} | Room Type: {rt.description} | Max Guests: {rt.max_guests} | "
                    f"Price: {room.price_per_night:.2f} CHF/night | Total: {total_price:.2f} CHF")
                
                facilities = facilities_manager.read_facilities_by_room(room)
                if facilities:
                    facility_names = [facility.facility_name for facility in facilities]
                    print(f"    Facilities: {', '.join(facility_names)}")
                else:
                    print(f"    Facilities: None")

    if not rooms_found:
        print(f"No available rooms found in '{input_city}' for {input_guest} guest(s) from {checkin} to {checkout}.")

def display_available_rooms_simple(hotels, room_manager, facilities_manager, input_city, checkin, checkout, input_guest, num_nights):
    if not hotels:
        print(f"No hotels found in '{input_city}'.")
        return

    print(f"\nAvailable rooms in {input_city} from {checkin} to {checkout} for {input_guest} guest(s) ({num_nights} nights):")
    
    rooms_found = False

    for hotel in hotels:
        available_rooms = room_manager.read_available_rooms_by_hotel(hotel, checkin, checkout)
        suitable_rooms = filter_suitable_rooms(available_rooms, input_guest)
        
        if suitable_rooms:
            rooms_found = True
            a = hotel.address
            print(f"\nHotel: {hotel.name} | Stars: {hotel.stars} | Street: {a.street} | City: {a.city} | ZIP: {a.zip_code}")
            
            for room in suitable_rooms:
                rt = room.room_type
                total_price = room.price_per_night * num_nights
                
                print(f"  Room {room.room_number} | Room Type: {rt.description} | Max Guests: {rt.max_guests} | "
                      f"Price: {room.price_per_night:.2f} CHF/night | Total: {total_price:.2f} CHF")
                
                facilities = facilities_manager.read_facilities_by_room(room)
                if facilities:
                    facility_names = [facility.facility_name for facility in facilities]
                    print(f"    Facilities: {', '.join(facility_names)}")
                else:
                    print(f"    Facilities: None")

    if not rooms_found:
        print(f"No available rooms found in '{input_city}' for {input_guest} guest(s) from {checkin} to {checkout}.")

def display_all_rooms_in_city(hotels, room_manager, facilities_manager, input_city):
    if not hotels:
        print(f"No hotels found in '{input_city}'.")
        return

    print(f"\nAll rooms in {input_city}:")
    
    rooms_found = False

    for hotel in hotels:
        all_rooms = room_manager.read_rooms_by_hotel(hotel)
        
        if all_rooms:
            rooms_found = True
            a = hotel.address
            print(f"\nHotel: {hotel.name} | Stars: {hotel.stars} | Street: {a.street} | City: {a.city} | ZIP: {a.zip_code}")
            
            for room in all_rooms:
                rt = room.room_type
                
                print(f"  Room {room.room_number} | Room Type: {rt.description} | Max Guests: {rt.max_guests} | "
                      f"Price: {room.price_per_night:.2f} CHF/night")
                
                facilities = facilities_manager.read_facilities_by_room(room)
                if facilities:
                    facility_names = [facility.facility_name for facility in facilities]
                    print(f"    Facilities: {', '.join(facility_names)}")
                else:
                    print(f"    Facilities: None")

    if not rooms_found:
        print(f"No rooms found in '{input_city}'.")