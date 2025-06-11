from __future__ import annotations
import model
from model.room_type import RoomType
from model.hotel import Hotel
from model.booking import Booking
from model.facilities import Facilities
from model.address import Address
from model.guest import Guest
from model.room import Room
from model.invoice import Invoice
from data_access.base_data_access import BaseDataAccess

class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_room_type(self, description: str, max_guests: int) -> RoomType:
        if description is None:
            raise ValueError("Room type description is required")
        if max_guests is None:
            raise ValueError("Max guests is required")

        sql = """
        INSERT INTO Room_Type (description, max_guests) VALUES (?, ?)
        """
        params = (description, max_guests)
        last_row_id, row_count = self.execute(sql, params)
        return RoomType(last_row_id, description, max_guests)

    def read_roomtype_by_id(self, type_id: int) -> RoomType:
        sql = """
        SELECT type_id, description, max_guests FROM Room_Type WHERE type_id = ?;
        """
        params = tuple([type_id])
        result = self.fetchone(sql, params)
        if result:
            type_id, description, max_guests = result
            return RoomType(type_id, description, max_guests)
        return None

    def read_room_type_by_description(self, description: str) -> RoomType | None:
        if description is None:
            raise ValueError("Description is required")

        sql = """
        SELECT type_id, description, max_guests FROM Room_Type WHERE description = ?
        """
        params = tuple([description])
        result = self.fetchone(sql, params)
        if result:
            type_id, description, max_guests = result
            return RoomType(type_id, description, max_guests)
        else:
            return None

    def read_all_room_types(self) -> list[RoomType]:
        sql = """
        SELECT type_id, description, max_guests FROM Room_Type ORDER BY max_guests, description
        """
        room_types = self.fetchall(sql)
        return [RoomType(type_id, description, max_guests)
                for type_id, description, max_guests in room_types]

    def read_room_types_by_guest_capacity(self, min_guests: int) -> list[RoomType]:
        if min_guests is None:
            raise ValueError("Minimum guests is required")

        sql = """
        SELECT type_id, description, max_guests FROM Room_Type WHERE max_guests >= ? ORDER BY max_guests
        """
        params = tuple([min_guests])
        room_types = self.fetchall(sql, params)
        return [RoomType(type_id, description, max_guests)
                for type_id, description, max_guests in room_types]

    def update_room_type(self, room_type: RoomType) -> None:
        if room_type is None:
            raise ValueError("Room type cannot be None")

        sql = """
        UPDATE Room_Type SET description = ?, max_guests = ? WHERE type_id = ?
        """
        params = tuple([room_type.description, room_type.max_guests, room_type.type_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_room_type(self, room_type: RoomType) -> None:
        if room_type is None:
            raise ValueError("Room type cannot be None")

        sql = """
        DELETE FROM Room_Type WHERE type_id = ?
        """
        params = tuple([room_type.type_id])
        last_row_id, row_count = self.execute(sql, params)