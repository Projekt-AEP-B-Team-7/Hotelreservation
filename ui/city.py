import json
import os

class CityValidationService:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "swiss_city_list.json")
        with open(path, "r", encoding="utf-8") as f:
            self.city_set = {city.lower() for city in json.load(f)}

    def is_valid_swiss_city(self, city: str) -> bool:
        return city.strip().lower() in self.city_set