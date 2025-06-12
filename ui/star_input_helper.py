def validate_star_input(input_stars):
    try:
        stars = int(input_stars)
        if 1 <= stars <= 5:
            return True, stars
        print("Please enter a value between 1 and 5 for star.")
        return False, None
    except ValueError:
        print("Please enter a number for the stars.")
        return False, None

def display_hotels_with_stars(hotels, input_city, input_stars):
    if not hotels:
        print(f"No hotels with {input_stars} stars found in '{input_city}'.")
    else:
        print(f"\nHotels in {input_city} with {input_stars} star:")
        for hotel in hotels:
            a = hotel.address
            print(f"Hotel: {hotel.name} | Stars: {hotel.stars} | Street: {a.street} | City: {a.city} | ZIP: {a.zip_code}")

def validate_star_range_input(input_stars):
    try:
        stars = int(input_stars)
        if 1 <= stars <= 5:
            return True, stars
        print("Stars must be between 1 and 5.")
        return False, None
    except ValueError:
        print("Please enter a valid number for stars.")
        return False, None

def display_available_hotels_with_criteria(hotels, input_city, input_stars, checkin, checkout, input_guest):
    if not hotels:
        print(f"\nNo hotels in '{input_city}' matching all your criteria. Please try again.")
    else:
        print(f"\nHotels in {input_city} with at least {input_stars} stars, "
              f"available from {checkin} to {checkout} for {input_guest} guest(s):")

        for hotel in hotels:
            a = hotel.address
            print(f"Hotel: {hotel.name} | Stars: {hotel.stars} | Street: {a.street} | City: {a.city} | ZIP: {a.zip_code}")