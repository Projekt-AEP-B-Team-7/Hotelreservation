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
    
    def read_available_rooms_by_date(self, hotel_id) -> model.Room
        sql = """
        SELECT room_id, hotel_id, room_number, type_id, price_per_night
        FROM Room 
        WHERE room_id NOT IN (
        SELECT room_id
        FROM Booking
        WHERE NOT (b.check_out_date <= ? OR b.check_in_date >= ?)
        )
        """
        params = (check_in, check_out)
        results = self.fetchall(sql, params)
        last_row_id, row_count = self.execute(sql, params)

    def get_rooms_with_facilities(self,type_id) -> model.Room
        sql = """
        SELECT 
        Room.room_id,
        Room.room_number,
        Room_Type.description AS room_type,
        Room.price_per_night,
        Facilities.name AS facility
        FROM Room
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        LEFT JOIN Room_Facilities ON Room.room_id = Room_Facilities.room_id
        LEFT JOIN Facilities ON Room_Facilities.facility_id = Facilities.facility_id
        ORDER BY Room.room_id, Facilities.name;
        """
        rows = self.fetchall(sql)

    #def update_room_price(self, room_id: int, new_price: float) -> model.Room
        sql = """
        "UPDATE Room SET price_per_night = ? WHERE room_id = ?"
        """
        self.execute(sql, (new_price, room_id))

    #def get_price_by_room_id(self, room_id: int) -> model.Room
        sql = """
        "SELECT price_per_night FROM Room WHERE room_id = ?"
        """
        row = self.fetchone(sql, (room_id,))
        return row[0] if row else None