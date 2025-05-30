from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class RoomtypeDataAccess(BaseDataAccess):
    
    def read_roomtype_by_id(self, type_id: int) -> model.Roomtype:
        sql = """
        SELECT type_id, description, max_guests  FROM Room WHERE type_id = ?;
        """
        params = tuple([type_id])
        result = self.fetchone(sql, params)
        if result:
            type_id, description, max_guests = result
            return model.Roomtype(type_id, description, max_guests)
        return None


   # def update_roomtype(self, type_id: int) -> model.Roomtype:
        if roomtype is None:
            raise ValueError("Roomtype cannot be None")

        sql = """
        UPDATE Roomtype SET price_per_night = ? WHERE room_id = ?
        """
        params = tuple([type_id])
        last_row_id, row_count = self.execute(sql, params)

    #def delete_roomtype(self, type_id: int) -> model.Roomtype
        if roomtype is None:
            raise ValueError("Hotel cannot be None")

        sql = """
        DELETE FROM Roomtype WHERE type_id = ?
        """
        params = tuple([type_id])
        last_row_id, row_count = self.execute(sql, params)

   # def insert_room_type(self, description: str, max_guests: int) -> model.Roomtype
        sql = """
        "INSERT INTO Room_Type (description, max_guests) VALUES (?, ?)"
        """
        return self.execute(sql, (description, max_guests))[0]