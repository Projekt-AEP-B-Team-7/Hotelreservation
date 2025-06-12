from ui.booking_helper import calculate_vat_amounts
from datetime import date

def display_all_bookings(bookings):
    print("\nAll current bookings:")
    print("=" * 120)
    
    if not bookings:
        print("There are no bookings to display.")
        return False, []
    
    active_bookings = [b for b in bookings if not b.is_cancelled]
    
    if not active_bookings:
        print("There are no active bookings to create invoices for.")
        return False, []
    
    return True, active_bookings

def display_booking_list(active_bookings, invoice_manager):
    for i, booking in enumerate(active_bookings, 1):
        guest_name = f"{booking.guest.first_name} {booking.guest.last_name}"
        hotel_name = booking.room.hotel.name
        
        net_amount = booking.total_amount
        vat_amount, gross_amount = calculate_vat_amounts(net_amount)
        
        existing_invoice = None
        try:
            existing_invoice = invoice_manager.read_invoice_by_booking(booking)
        except:
            pass
        
        invoice_status = "INVOICE EXISTS" if existing_invoice else "NO INVOICE"
        
        print(f"{i}. Guest: {guest_name} | "
              f"Hotel: {hotel_name} | Room: {booking.room.room_number} | "
              f"Check-in: {booking.check_in_date} | Check-out: {booking.check_out_date} | "
              f"Net: {net_amount:.2f} CHF | Total incl. VAT: {gross_amount:.2f} CHF | {invoice_status}")

def validate_booking_choice(choice_str, active_bookings):
    try:
        choice = int(choice_str)
        if choice < 1 or choice > len(active_bookings):
            print(f"Please enter a number between 1 and {len(active_bookings)}.")
            return False, None
        return True, choice - 1
    except ValueError:
        print("Please enter a valid number from the list above.")
        return False, None

def check_existing_invoice(invoice_manager, selected_booking):
    try:
        existing_invoice = invoice_manager.read_invoice_by_booking(selected_booking)
        return existing_invoice
    except:
        return None

def display_existing_invoice(existing_invoice, selected_booking):
    print(f"\nInvoice already exists for this booking:")
    print(f"Invoice ID: {existing_invoice.invoice_id}")
    print(f"Issue Date: {existing_invoice.issue_date}")
    print(f"First Name: {selected_booking.guest.first_name}")
    print(f"Last Name: {selected_booking.guest.last_name}")
    print(f"Hotel: {selected_booking.room.hotel.name}")
    if selected_booking.room.hotel.address:
        print(f"City: {selected_booking.room.hotel.address.city}")
    print(f"Check-in: {selected_booking.check_in_date}")
    print(f"Check-out: {selected_booking.check_out_date}")

    existing_net = existing_invoice.total_amount
    existing_vat, existing_gross = calculate_vat_amounts(existing_net)
    
    print(f"Net Amount: {existing_net:.2f} CHF")
    print(f"VAT (3.8%): {existing_vat:.2f} CHF")
    print(f"Total Amount: {existing_gross:.2f} CHF")

def create_and_display_invoice(invoice_manager, selected_booking):
    try:
        issue_date = date.today()
        net_amount = selected_booking.total_amount
        vat_amount, gross_amount = calculate_vat_amounts(net_amount)
    
        invoice = invoice_manager.create_invoice(selected_booking, issue_date, gross_amount)
        
        nights = (selected_booking.check_out_date - selected_booking.check_in_date).days
        
        print(f"\nInvoice successfully created!")
        print("=" * 70)
        print(f"INVOICE DETAILS")
        print("=" * 70)
        print(f"Invoice ID: {invoice.invoice_id}")
        print(f"Issue Date: {invoice.issue_date}")
        print()
        print(f"GUEST INFORMATION")
        print("-" * 30)
        print(f"Guest: {selected_booking.guest.first_name} {selected_booking.guest.last_name}")
        print(f"Email: {selected_booking.guest.email}")
        if selected_booking.guest.phone_number:
            print(f"Phone: {selected_booking.guest.phone_number}")
        print()
        print(f"ACCOMMODATION DETAILS")
        print("-" * 30)
        print(f"Hotel: {selected_booking.room.hotel.name}")
        print(f"Room: {selected_booking.room.room_number} ({selected_booking.room.room_type.description})")
        print(f"Check-in: {selected_booking.check_in_date}")
        print(f"Check-out: {selected_booking.check_out_date}")
        print(f"Number of nights: {nights}")
        print()
        print(f"BILLING BREAKDOWN")
        print("-" * 30)
        print(f"Price per night: {selected_booking.room.price_per_night:.2f} CHF")
        print(f"Net amount ({nights} nights): {net_amount:.2f} CHF")
        print(f"VAT (3.8%): {vat_amount:.2f} CHF")
        print("=" * 40)
        print(f"TOTAL AMOUNT: {gross_amount:.2f} CHF")
        print("=" * 70)
        print("Thank you for choosing our hotel!")
        
        return True, invoice
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print(f"Error details: {type(e).__name__}")
        return False, None