from datetime import datetime

def get_valid_date_input(prompt_text: str) -> str:
    while True:
        date_str = input(prompt_text).strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")