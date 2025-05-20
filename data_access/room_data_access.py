from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class RoomDataAccess(BaseDataAccess):
    
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_room_by_hotel_id(self, hotel_id: int) -> model.Room | None:
        sql = """
        SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM Room WHERE hotel_id = ?;
        """
        params = tuple([hotel_id])
        result = self.fetchone(sql, params)
        if result:
            room_id, hotel_id, room_number, type_id, price_per_night = result
            return model.Room(room_id, hotel_id, room_number, type_id, price_per_night)
        else:
            return None

    def update_room_price(self, room_id: int) -> model.Room:
        if room is None:
            raise ValueError("Room cannot be None")

        sql = """
        UPDATE Room SET price_per_night = ? WHERE room_id = ?
        """
        params = tuple([room_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_room(self, room_id: int) -> model.Room:
        if room is None:
            raise ValueError("Hotel cannot be None")

        sql = """
        DELETE FROM Room WHERE room_id = ?
        """
        params = tuple([room_id])
        last_row_id, row_count = self.execute(sql, params)
    