def get_address_inputs():
    street = input("Street: ")
    city = input("City: ").strip()
    zip_code = input("ZIP code: ")
    return street, city, zip_code

def validate_and_create_address(address_manager, street, city, zip_code):
    try:
        address = address_manager.create_address(street, city, zip_code)
        return True, address
    except Exception as e:
        print(f"Error while saving address: {e}")
        return False, None