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