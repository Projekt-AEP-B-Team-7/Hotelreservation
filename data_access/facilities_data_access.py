from __future__ import annotations
from model.facilities import Facilities
from model.room import Room
from data_access.base_data_access import BaseDataAccess

class FacilitiesDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_facility(self, facility_name: str) -> Facilities:
        if facility_name is None:
            raise ValueError("Facility name is required")

        sql = """
        INSERT INTO Facilities (facility_name) VALUES (?)
        """
        params = tuple([facility_name])
        last_row_id, row_count = self.execute(sql, params)
        return Facilities(last_row_id, facility_name)

    def read_facility_by_id(self, facility_id: int) -> Facilities | None:
        if facility_id is None:
            raise ValueError("Facility ID is required")

        sql = """
        SELECT facility_id, facility_name FROM Facilities WHERE facility_id = ?
        """
        params = tuple([facility_id])
        result = self.fetchone(sql, params)
        if result:
            facility_id, facility_name = result
            return Facilities(facility_id, facility_name)
        else:
            return None

    def read_facility_by_name(self, facility_name: str) -> Facilities | None:
        if facility_name is None:
            raise ValueError("Facility name is required")

        sql = """
        SELECT facility_id, facility_name FROM Facilities WHERE facility_name = ?
        """
        params = tuple([facility_name])
        result = self.fetchone(sql, params)
        if result:
            facility_id, facility_name = result
            return Facilities(facility_id, facility_name)
        else:
            return None

    def read_all_facilities(self) -> list[Facilities]:
        sql = """
        SELECT facility_id, facility_name FROM Facilities ORDER BY facility_name
        """
        facilities = self.fetchall(sql)
        return [Facilities(facility_id, facility_name)
            for facility_id, facility_name in facilities]

    def read_facilities_by_room(self, room: Room) -> list[Facilities]:
        if room is None:
            raise ValueError("Room cannot be None")

        sql = """
        SELECT Facilities.facility_id, Facilities.facility_name
        FROM Facilities
        JOIN Room_Facilities ON Facilities.facility_id = Room_Facilities.facility_id
        WHERE Room_Facilities.room_id = ?
        ORDER BY Facilities.facility_name
        """
        params = tuple([room.room_id])
        facilities = self.fetchall(sql, params)
        
        return [Facilities(facility_id, facility_name)
            for facility_id, facility_name in facilities]

    def read_facilities_like_name(self, facility_name: str) -> list[Facilities]:
        if facility_name is None:
            raise ValueError("Facility name is required")

        sql = """
        SELECT facility_id, facility_name FROM Facilities WHERE facility_name LIKE ? ORDER BY facility_name
        """
        params = tuple([f"%{facility_name}%"])
        facilities = self.fetchall(sql, params)
        return [Facilities(facility_id, facility_name)
            for facility_id, facility_name in facilities]

    def add_facility_to_room(self, room: Room, facility: Facilities) -> None:
        if room is None:
            raise ValueError("Room cannot be None")
        if facility is None:
            raise ValueError("Facility cannot be None")

        sql = """
        INSERT INTO Room_Facilities (room_id, facility_id) VALUES (?, ?)
        """
        params = tuple([room.room_id, facility.facility_id])
        last_row_id, row_count = self.execute(sql, params)

    def remove_facility_from_room(self, room: Room, facility: Facilities) -> None:
        if room is None:
            raise ValueError("Room cannot be None")
        if facility is None:
            raise ValueError("Facility cannot be None")

        sql = """
        DELETE FROM Room_Facilities WHERE room_id = ? AND facility_id = ?
        """
        params = tuple([room.room_id, facility.facility_id])
        last_row_id, row_count = self.execute(sql, params)

    def update_facility(self, facility: Facilities) -> None:
        if facility is None:
            raise ValueError("Facility cannot be None")

        sql = """
        UPDATE Facilities SET facility_name = ? WHERE facility_id = ?
        """
        params = tuple([facility.facility_name, facility.facility_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_facility(self, facility: Facilities) -> None:
        if facility is None:
            raise ValueError("Facility cannot be None")

        sql = """
        DELETE FROM Facilities WHERE facility_id = ?
        """
        params = tuple([facility.facility_id])
        last_row_id, row_count = self.execute(sql, params)