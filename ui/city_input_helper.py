#Fragt den Benutzer nach einer gültigen Schweizer Stadt und wiederholt, bis eine gültige Eingabe erfolgt ist.

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