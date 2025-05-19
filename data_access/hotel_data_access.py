from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class HotelDataAccess(BaseDataAccess):
    
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_hotel_by_name(self, name: str) -> model.Hotel | None:
        sql = """
        SELECT HotelId, Name, Stars FROM Hotel WHERE Name = ?;
        """
        params = tuple([name])
        result = self.fetchone(sql, params)
        if result:
            hotel_id, name, stars = result
            return model.Hotel(hotel_id, name, stars)
        else:
            return None

    def read_hotel_by_city(self, city: str) -> model.Hotel | None:
        sql = """
        SELECT HotelId, Name, City, Stars FROM Hotel WHERE City = ?;
        """
        params = tuple([city])
        result = self.fetchone(sql, params)
        if result:
            hotel_id, name, city, stars = result
            return model.Hotel(hotel_id, name, city, stars)
        else:
            return None
    
    def read_hotel_by_star(self, star: int) -> model.Hotel | None:
        sql = """
        SELECT HotelId, Name, City, Stars FROM Hotel WHERE Stars = ?;
        """
        params = tuple([star])
        result = self.fetchone(sql, params)
        if result:
            hotel_id, name, city, stars = result
            return model.Hotel(hotel_id, name, city, stars)
        else:
            return None
    