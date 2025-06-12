def get_hotel_name_input():
    return input("Hotel name: ")

def validate_hotel_creation(hotel_manager, name, stars, address):
    try:
        hotel = hotel_manager.create_hotel(name, stars, address)
        print(f"Hotel created successfully: {hotel}")
        return True
    except Exception as e:
        print(f"Error while creating hotel: {e}")
        return False

def display_hotel_selection(all_hotels):
    print("\nAvailable Hotels:")
    for i, hotel in enumerate(all_hotels, 1):
        print(f"{i}. {hotel.name}")

def display_hotels_with_details(hotels):
    print("All Hotels:")
    for i, hotel in enumerate(hotels, 1):
        address_info = f"{hotel.address.city}" if hotel.address else "No address"
        print(f"{i}. Name: {hotel.name} | Stars: {hotel.stars} | City: {address_info}")

def validate_hotel_selection(selection_str, all_hotels):
    try:
        selection = int(selection_str)
        idx = selection - 1
        if 0 <= idx < len(all_hotels):
            return True, idx
        else:
            print(f"Please enter a number between 1 and {len(all_hotels)}.")
            return False, None
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return False, None

def display_hotel_info(hotel):
    print(f"\nSelected hotel: {hotel.name}")
    print(f"Current hotel info:")
    print(f"Name: {hotel.name}")
    print(f"Stars: {hotel.stars}")
    if hotel.address:
        print(f"Address: Street: {hotel.address.street}, Zip code: {hotel.address.zip_code}, City: {hotel.address.city}")
    else:
        print("Address: No address")

def display_update_menu():
    print(f"\nWhat would you like to change?")
    print("1. Hotel Name")
    print("2. Stars")
    print("3. Address Street")
    print("4. Zip code")
    print("5. City")

def validate_update_choice(choice_str):
    try:
        choice = int(choice_str)
        if 1 <= choice <= 5:
            return True, choice
        else:
            print("Invalid choice.")
            return False, None
    except ValueError:
        print("Invalid choice.")
        return False, None

def update_hotel_name(hotel, hotel_manager):
    new_name = input(f"Enter new name (current: {hotel.name}): ")
    if new_name:
        hotel.name = new_name
        hotel_manager.update_hotel(hotel)
        print("Hotel name updated.")

def update_hotel_stars(hotel, hotel_manager):
    try:
        new_stars = int(input(f"Enter new stars (current: {hotel.stars}): "))
        if 1 <= new_stars <= 5:
            hotel.stars = new_stars
            hotel_manager.update_hotel(hotel)
            print("Hotel stars updated.")
        else:
            print("Stars must be between 1 and 5.")
    except ValueError:
        print("Please enter a valid number.")

def update_hotel_street(hotel, hotel_manager):
    if hotel.address:
        new_street = input(f"Enter new street (current: {hotel.address.street}): ")
        if new_street:
            hotel.address.street = new_street
            hotel_manager.update_hotel(hotel)
            print("Hotel street updated.")
    else:
        print("No address found.")

def update_hotel_zip(hotel, hotel_manager):
    if hotel.address:
        new_zip = input(f"Enter new zip code (current: {hotel.address.zip_code}): ")
        if new_zip:
            hotel.address.zip_code = new_zip
            hotel_manager.update_hotel(hotel)
            print(f"Hotel zip code updated: {new_zip}.")
    else:
        print("No address found.")

def update_hotel_city(hotel, hotel_manager, city_validator):
    if hotel.address:
        current_city = hotel.address.city
        print(f"Current city: {current_city}")
        
        valid_city = False
        while not valid_city:
            new_city = input("Enter new city (Swiss city only): ")
            if new_city:
                if city_validator.is_valid_swiss_city(new_city):
                    hotel.address.city = new_city
                    hotel_manager.update_hotel(hotel)
                    print(f"Hotel city updated: {new_city}.")
                    valid_city = True
                else:
                    print(f"'{new_city}' is not a valid Swiss city. Please try again.")
            else:
                print("No changes made.")
                valid_city = True
    else:
        print("No address found.")

def validate_delete_confirmation(confirm):
    if confirm in ["y", "yes"]:
        return True
    else:
        print("Hotel deletion cancelled.")
        return False

def delete_hotel_with_error_handling(hotel_manager, selected_hotel):
    try:
        hotel_manager.delete_hotel(selected_hotel)
        print(f"Hotel '{selected_hotel.name}' (ID: {selected_hotel.hotel_id}) was successfully deleted.")
        return True
    except Exception as e:
        print(f"Error while deleting the hotel: {e}")
        return False