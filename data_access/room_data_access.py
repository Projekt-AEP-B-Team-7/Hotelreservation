from __future__ import annotations
import model
from data_access.base_data_access import BaseDataAccess

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_room(self, hotel: model.Hotel, room_number: str, room_type: model.RoomType, price_per_night: float) -> model.Room:
        if hotel is None:
            raise ValueError("Hotel is required")
        if room_number is None:
            raise ValueError("Room number is required")
        if room_type is None:
            raise ValueError("Room type is required")
        if price_per_night is None:
            raise ValueError("Price per night is required")

        sql = """
        INSERT INTO Room (hotel_id, room_number, type_id, price_per_night) VALUES (?, ?, ?, ?)
        """
        params = (hotel.hotel_id, room_number, room_type.type_id, price_per_night)
        last_row_id, row_count = self.execute(sql, params)
        return model.Room(last_row_id, hotel, room_number, room_type, price_per_night)

