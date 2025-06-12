VAT_RATE = 0.038  # 3.8%

def calculate_vat_amounts(net_amount: float):
    """Berechnet MwSt und Bruttobetrag"""
    vat_amount = net_amount * VAT_RATE
    gross_amount = net_amount + vat_amount
    return vat_amount, gross_amount

def calculate_vat_from_gross(gross_amount: float):
    """Berechnet Netto und MwSt aus Bruttobetrag"""
    net_amount = gross_amount / (1 + VAT_RATE)
    vat_amount = gross_amount - net_amount
    return net_amount, vat_amount

def get_or_create_guest(guest_manager, first_name, last_name, email, phone):
    """Prüft ob Gast bereits existiert, erstellt neuen falls nicht"""
    try:
        existing_guest = guest_manager.read_guest_by_email(email)
        if existing_guest:
            print(f"Found existing guest: {existing_guest.first_name} {existing_guest.last_name}")
            
            update_info = input("Do you want to update the guest information? (y/n): ").strip().lower()
            if update_info in ['y', 'yes']:
                existing_guest.first_name = first_name
                existing_guest.last_name = last_name
                existing_guest.phone_number = phone
                guest_manager.update_guest(existing_guest)
                print("Guest information updated.")
            
            return existing_guest
    except:
        pass
    
    try:
        new_guest = guest_manager.create_new_guest_w_phone_nr(first_name, last_name, email, phone)
        print(f"Created new guest: {new_guest.first_name} {new_guest.last_name}")
        return new_guest
    except Exception as e:
        print(f"Error creating guest: {e}")
        raise

def display_available_rooms_for_booking(hotels, room_manager, input_city, checkin, checkout, input_guest, num_nights):
    print(f"\nAvailable rooms in {input_city} from {checkin} to {checkout} for {input_guest} guest(s) ({num_nights} nights):")
    
    available_hotels = []
    rooms_found = False

    for hotel in hotels:
        available_rooms = room_manager.read_available_rooms_by_hotel(hotel, checkin, checkout)
        
        suitable_rooms = []
        for room in available_rooms:
            if room.room_type and room.room_type.max_guests >= input_guest:
                suitable_rooms.append(room)
        
        if suitable_rooms:
            rooms_found = True
            available_hotels.append((hotel, suitable_rooms))
            a = hotel.address
            print(f"\nHotel: {hotel.name} | Stars: {hotel.stars} | Street: {a.street} | City: {a.city} | ZIP: {a.zip_code}")
            
            for room in suitable_rooms:
                rt = room.room_type
                net_total = room.price_per_night * num_nights
                vat_amount, gross_total = calculate_vat_amounts(net_total)
                
                print(f"  Room {room.room_number} | Room Type {rt.description} | Max Guests: {rt.max_guests}")
                print(f"    Price: {room.price_per_night:.2f} CHF/night")
                print(f"    Net total ({num_nights} nights): {net_total:.2f} CHF")
                print(f"    VAT (3.8%): {vat_amount:.2f} CHF")
                print(f"    Total incl. VAT: {gross_total:.2f} CHF")

    return rooms_found, available_hotels

def validate_booking_choice(book_now):
    if book_now in ['y', 'yes']:
        return True
    elif book_now in ['n', 'no']:
        return False
    else:
        print("Please enter 'y' for yes or 'n' for no.")
        return None

def display_hotel_selection_for_booking(available_hotels):
    print("\nSelect a hotel:")
    for i, (hotel, rooms) in enumerate(available_hotels, 1):
        print(f"{i}. {hotel.name} ({hotel.stars} stars)")

def validate_hotel_choice(hotel_choice_str, available_hotels):
    try:
        hotel_choice = int(hotel_choice_str) - 1
        if 0 <= hotel_choice < len(available_hotels):
            return True, hotel_choice
        else:
            print(f"Please enter a number between 1 and {len(available_hotels)}.")
            return False, None
    except ValueError:
        print("Please enter a valid number.")
        return False, None

def display_room_selection_for_booking(selected_hotel, selected_hotel_rooms, num_nights):
    print(f"\nAvailable rooms in {selected_hotel.name}:")
    for i, room in enumerate(selected_hotel_rooms, 1):
        rt = room.room_type
        net_total = room.price_per_night * num_nights
        vat_amount, gross_total = calculate_vat_amounts(net_total)
        
        print(f"{i}. Room {room.room_number} - {rt.description}")
        print(f"   {room.price_per_night:.2f} CHF/night - Total incl. VAT: {gross_total:.2f} CHF")

def validate_room_choice(room_choice_str, selected_hotel_rooms):
    try:
        room_choice = int(room_choice_str) - 1
        if 0 <= room_choice < len(selected_hotel_rooms):
            return True, room_choice
        else:
            print(f"Please enter a number between 1 and {len(selected_hotel_rooms)}.")
            return False, None
    except ValueError:
        print("Please enter a valid number.")
        return False, None

def get_guest_details():
    print("\nPlease enter guest details:")
    first = input("First name: ")
    last = input("Last name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    return first, last, email, phone

def create_booking_with_confirmation(booking_manager, guest, selected_room, checkin_date, checkout_date, gross_amount, selected_hotel, checkin, checkout, num_nights):
    try:
        booking = booking_manager.create_booking(guest, selected_room, checkin_date, checkout_date, gross_amount)
        
        net_amount = num_nights * selected_room.price_per_night
        vat_amount, gross_total = calculate_vat_amounts(net_amount)
        
        print("\nBooking successfully created!")
        print("=" * 50)
        print(f"Booking ID: {booking.booking_id}")
        print(f"Guest: {guest.first_name} {guest.last_name}")
        print(f"Email: {guest.email}")
        print(f"Phone: {guest.phone_number}")
        print(f"Hotel: {selected_hotel.name}")
        print(f"Room: {selected_room.room_number} ({selected_room.room_type.description})")
        print(f"Stay: {checkin} to {checkout} ({num_nights} nights)")
        print()
        print("BILLING BREAKDOWN:")
        print("-" * 30)
        print(f"Price per night: {selected_room.price_per_night:.2f} CHF")
        print(f"Net amount ({num_nights} nights): {net_amount:.2f} CHF")
        print(f"VAT (3.8%): {vat_amount:.2f} CHF")
        print("=" * 30)
        print(f"TOTAL AMOUNT: {gross_total:.2f} CHF")
        print("=" * 50)
        
        return True, booking
    except Exception as e:
        print(f"Error creating booking: {e}")
        print("Please try again.")
        return False, None

def display_active_bookings_for_cancellation(bookings, invoice_manager):
    print("BOOKING CANCELLATION")
    print("=" * 60)
    print("All current active bookings:")
    print("=" * 120)
    
    if not bookings:
        print("There are no bookings to display.")
        return False, []
    
    active_bookings = [b for b in bookings if not b.is_cancelled]
    
    if not active_bookings:
        print("There are no active bookings to cancel.")
        return False, []
    
    for i, booking in enumerate(active_bookings, 1):
        guest_name = f"{booking.guest.first_name} {booking.guest.last_name}"
        hotel_name = booking.room.hotel.name
        city = booking.room.hotel.address.city if booking.room.hotel.address else "N/A"
        
        gross_amount = booking.total_amount
        net_amount, vat_amount = calculate_vat_from_gross(gross_amount)
        
        invoice_exists = False
        try:
            existing_invoice = invoice_manager.read_invoice_by_booking(booking)
            invoice_exists = existing_invoice is not None
        except:
            pass
        
        invoice_status = "INVOICE EXISTS" if invoice_exists else "NO INVOICE"
        
        print(f"{i}. Guest: {guest_name} | Hotel: {hotel_name} ({city}) | "
              f"Room: {booking.room.room_number} | {booking.check_in_date} to {booking.check_out_date} | "
              f"Total: {gross_amount:.2f} CHF | {invoice_status}")
    
    return True, active_bookings

def validate_cancellation_choice(choice_str, active_bookings):
    try:
        choice = int(choice_str)
        if choice < 1 or choice > len(active_bookings):
            print(f"Please enter a number between 1 and {len(active_bookings)}.")
            return False, None
        return True, choice - 1
    except ValueError:
        print("Please enter a valid number from the list above.")
        return False, None

def display_cancellation_details(selected_booking):
    guest_name = f"{selected_booking.guest.first_name} {selected_booking.guest.last_name}"
    hotel_name = selected_booking.room.hotel.name
    city = selected_booking.room.hotel.address.city if selected_booking.room.hotel.address else "N/A"
    
    gross_amount = selected_booking.total_amount
    net_amount, vat_amount = calculate_vat_from_gross(gross_amount)
    nights = (selected_booking.check_out_date - selected_booking.check_in_date).days
    
    print(f"\nBooking details to cancel:")
    print("-" * 40)
    print(f"Booking ID: {selected_booking.booking_id}")
    print(f"Guest: {guest_name}")
    print(f"Email: {selected_booking.guest.email}")
    print(f"Hotel: {hotel_name} ({city})")
    print(f"Room: {selected_booking.room.room_number} ({selected_booking.room.room_type.description})")
    print(f"Stay: {selected_booking.check_in_date} to {selected_booking.check_out_date} ({nights} nights)")
    print(f"Net amount: {net_amount:.2f} CHF")
    print(f"VAT (3.8%): {vat_amount:.2f} CHF")
    print(f"Total amount: {gross_amount:.2f} CHF")

def validate_cancellation_confirmation(confirm):
    if confirm in ['y', 'yes']:
        return True
    elif confirm in ['n', 'no']:
        print("Booking cancellation was aborted.")
        return False
    else:
        print("Invalid input. Booking cancellation was aborted.")
        return False

def cancel_booking_with_invoice_cleanup(booking_manager, invoice_manager, selected_booking):
    try:
        existing_invoice = None
        try:
            existing_invoice = invoice_manager.read_invoice_by_booking(selected_booking)
        except:
            pass
       
        success = booking_manager.cancel_booking_by_id(selected_booking.booking_id)
        
        if success:
            print("\nBooking successfully cancelled!")

            if existing_invoice:
                try:
                    invoice_manager.delete_invoice(existing_invoice)
                    print(f"Associated invoice (ID: {existing_invoice.invoice_id}) has been deleted.")
                except Exception as e:
                    print(f"Warning: Could not delete invoice - {e}")
            else:
                print("No associated invoice found to delete.")
            
            guest_name = f"{selected_booking.guest.first_name} {selected_booking.guest.last_name}"
            hotel_name = selected_booking.room.hotel.name
            gross_amount = selected_booking.total_amount
            
            print("-" * 50)
            print("CANCELLATION SUMMARY:")
            print(f"Cancelled Booking ID: {selected_booking.booking_id}")
            print(f"Guest: {guest_name}")
            print(f"Hotel: {hotel_name}")
            print(f"Refund amount: {gross_amount:.2f} CHF")
            print("-" * 50)
            print("The booking has been cancelled and you will not be charged.")
            
            return True
        else:
            print("Error: Booking could not be cancelled or was already cancelled.")
            return False
            
    except Exception as e:
        print(f"An error occurred while cancelling the booking: {e}")
        return False