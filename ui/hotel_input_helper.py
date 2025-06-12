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