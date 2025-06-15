def display_admin_booking_menu():
    print("Admin Booking Overview - Select view:")
    print("1. All bookings")
    print("2. Active bookings only")
    print("3. Cancelled bookings only")

def validate_admin_menu_choice(choice_str):
    try:
        view_choice = int(choice_str)
        if 1 <= view_choice <= 3:
            return True, view_choice
        print("Please choose 1, 2, or 3.")
        return False, None
    except ValueError:
        print("Please enter a valid number.")
        return False, None

def get_bookings_by_choice(booking_manager, view_choice):
    if view_choice == 1:
        bookings = booking_manager.read_all_bookings()
        title = "All Bookings"
    elif view_choice == 2:
        bookings = booking_manager.read_active_bookings()
        title = "Active Bookings"
    elif view_choice == 3:
        bookings = booking_manager.read_cancelled_bookings()
        title = "Cancelled Bookings"
    
    return bookings, title

def display_admin_booking_overview(bookings, title):
    if not bookings:
        print(f"\nNo {title.lower()} found.")
        return False
    
    print(f"\n{title}: {len(bookings)} booking(s)")
    print("="*120)
    
    for booking in bookings:
        status = "CANCELLED" if booking.is_cancelled else "ACTIVE"
        guest_name = f"{booking.guest.first_name} {booking.guest.last_name}"
        hotel_name = booking.room.hotel.name
        
        print(f"Booking ID: {booking.booking_id} | Guest: {guest_name} | Email: {booking.guest.email} | "
              f"Hotel: {hotel_name} | Room: {booking.room.room_number} | Type: {booking.room.room_type.description} | "
              f"Check-in: {booking.check_in_date} | Check-out: {booking.check_out_date} | "
              f"Amount: {booking.total_amount:.2f} CHF | Status: {status}")
    
    return True

def validate_view_again_choice(search_again):
    if search_again in ['y', 'yes']:
        return True
    elif search_again in ['n', 'no']:
        print("Admin session ended.")
        return False
    else:
        print("Please enter 'y' for yes or 'n' for no.")
        return None

def get_room_type_menu_choice():
    print("\nRoom Type Admin")
    print("1. Show all room types")
    print("2. Add new room type")
    print("3. Update room type")
    print("4. Delete room type")
    print("5. Exit")
    return input("Enter your choice: ").strip()

def input_room_type_data():
    desc = input("Enter room type description: ").strip()
    guests = int(input("Enter max guests: "))
    return desc, guests

def display_all_room_types_with_index(room_types):
    for i, t in enumerate(room_types, 1):
        print(f"\n{i}. Description: {t.description}, Max Guests: {t.max_guests}")

def validate_room_type_choice(choice_str, room_types):
    if choice_str.isdigit():
        idx = int(choice_str) - 1
        if 0 <= idx < len(room_types):
            return True, idx
    return False, None

def display_room_type(rt):
    print(f"\nID: {rt.type_id} | Description: {rt.description} | Max Guests: {rt.max_guests}")

def get_facility_menu_choice():
    print("\nFacility Admin")
    print("1. Show all facilities")
    print("2. Add new facility")
    print("3. Update facility")
    print("4. Delete facility")
    print("5. Exit")
    return input("Enter your choice: ").strip()

def input_facility_name():
    return input("Enter facility name: ").strip()

def display_all_facilities_with_index(facilities):
    for i, f in enumerate(facilities, 1):
        print(f"{i}. Name: {f.facility_name}")

def validate_facility_choice(choice_str, facilities):
    if choice_str.isdigit():
        idx = int(choice_str) - 1
        if 0 <= idx < len(facilities):
            return True, idx
    return False, None

def display_facility(fac):
    print(f"ID: {fac.facility_id} | Name: {fac.facility_name}")