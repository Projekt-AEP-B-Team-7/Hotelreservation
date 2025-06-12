def get_valid_swiss_city_input(city_validator) -> str:
    while True:
        input_city = input("In which city are you looking for a hotel? ").strip()

        if not input_city:
            print("Please enter a city name.")
            continue

        if not city_validator.is_valid_swiss_city(input_city):
            print(f"'{input_city}' is not a valid Swiss city. Please try again.")
            continue

        return input_city

def validate_city_input(input_city, city_validator):
    if not input_city:
        print("Please enter a city name.")
        return False
        
    if not city_validator.is_valid_swiss_city(input_city):
        print(f"'{input_city}' is not a valid Swiss city. Please try again.")
        return False
        
    return True

def validate_continue_choice(search_again):
    if search_again in ['y', 'yes']:
        return True, True
    elif search_again in ['n', 'no']:
        print("Program ended.")
        return True, False
    else:
        print("Please enter 'y' for yes or 'n' for no.")
        return False, None

def display_hotels(hotels, input_city):
    if hotels:
        print(f"\nFound hotels in {input_city}:")
        for hotel in hotels:
            a = hotel.address
            print(f"Hotel: {hotel.name} | Stars: {hotel.stars} | Street: {a.street} | City: {a.city} | ZIP: {a.zip_code}")
    else:
        print(f"No hotels found in '{input_city}'. Please try another city.")

def normalize_city_name(input_city, city_validator):
    import json
    import os
    
    path = os.path.join(os.path.dirname(__file__), "swiss_city_list.json")
    with open(path, "r", encoding="utf-8") as f:
        city_list = json.load(f)
    
    input_lower = input_city.lower()
    for city in city_list:
        if city.lower() == input_lower:
            return city
    return input_city

def validate_city_exists_in_database(input_city, hotel_manager):
    if hotel_manager.city_exists_in_database(input_city):
        return True
    print(f"No hotels found in '{input_city}'. Try another city.")
    return False

def display_available_hotels_with_dates(hotels, input_city, checkin, checkout, input_guest):
    if not hotels:
        print(f"\nNo available hotels in '{input_city}' from {checkin} to {checkout} for {input_guest} guest(s).")
    else:
        print(f"\nAvailable hotels in {input_city} from {checkin} to {checkout} for {input_guest} guest(s):")
        for hotel in hotels:
            a = hotel.address
            print(f"Hotel: {hotel.name} | Stars: {hotel.stars} | Street: {a.street} | City: {a.city} | ZIP: {a.zip_code}")
            
def validate_add_another_choice(add_another):
    if add_another in ['y', 'yes']:
        return True, True
    elif add_another in ['n', 'no']:
        print("Program ended.")
        return True, False
    else:
        print("Please enter 'y' for yes or 'n' for no.")
        return False, None