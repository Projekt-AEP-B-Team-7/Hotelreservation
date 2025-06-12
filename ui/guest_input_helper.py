def get_valid_guest_input(prompt_text: str) -> int:
    while True:
        try:
            guests = int(input(prompt_text).strip())
            if guests < 1:
                print("Number of guests must be at least 1.")
                continue
            return guests
        except ValueError:
            print("Please enter a valid number of guests.")

def validate_guest_input(input_guest):
    try:
        guests = int(input_guest)
        if guests < 1:
            print("Number of guests must be at least 1.")
            return False, None
        return True, guests
    except ValueError:
        print("Please enter a valid number for guests.")
        return False, None

def display_hotels_by_capacity(hotels, input_city, input_guest):
    if not hotels:
        print(f"No suitable hotels found in '{input_city}' for {input_guest} guest(s).")
    else:
        print(f"\nFound Hotels in {input_city} for {input_guest} guest(s):")
        for hotel in hotels:
            a = hotel.address
            print(f"Hotel: {hotel.name} | Stars: {hotel.stars} | Street: {a.street} | City: {a.city} | ZIP: {a.zip_code}")