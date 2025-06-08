from datetime import datetime, date

class DateInputHelper:
    def __init__(self):
        self.today = date.today()

    def get_valid_date_input(self, prompt: str, allow_past_dates: bool = False) -> str:
        while True:
            user_input = input(prompt).strip()
            if not user_input:
                print("Please enter a date.")
                continue

            try:
                parsed_date = datetime.strptime(user_input, '%Y-%m-%d').date()

                if not allow_past_dates and parsed_date < self.today:
                    print(f"Date cannot be in the past. Today is {self.today}. Please enter a future date.")
                    continue

                return user_input
            except ValueError:
                print("Please enter the date in YYYY-MM-DD format (e.g., 2025-06-15).")

    def get_valid_checkin_date(self) -> str:
        return self.get_valid_date_input("Check-in date (YYYY-MM-DD): ", allow_past_dates=False)

    def get_valid_checkout_date(self, checkin_date: str = None) -> str:
        if checkin_date:
            checkin = datetime.strptime(checkin_date, '%Y-%m-%d').date()

            while True:
                checkout_str = self.get_valid_date_input("Check-out date (YYYY-MM-DD): ", allow_past_dates=False)
                checkout = datetime.strptime(checkout_str, '%Y-%m-%d').date()

                if checkout > checkin:
                    return checkout_str
                else:
                    print(f"Check-out date must be after check-in date ({checkin_date}).")
        else:
            return self.get_valid_date_input("Check-out date (YYYY-MM-DD): ", allow_past_dates=False)

    def get_valid_date_range(self) -> tuple[str, str]:
        checkin = self.get_valid_checkin_date()
        checkout = self.get_valid_checkout_date(checkin)
        return checkin, checkout

    def get_valid_date_input_old(self, prompt: str) -> str:
        return self.get_valid_date_input(prompt, allow_past_dates=True)