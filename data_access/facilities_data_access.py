from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class FacilitiesDataAccess(BaseDataAccess):
    
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_facilities_name(self, facility_name: str) -> model.Facilities | None:
        sql = """
        SELECT facility_id, facility_name FROM Facilities WHERE facility_name = ?;
        """
        params = tuple([facility_name])
        result = self.fetchone(sql, params)
        if result:
            facility_id, facility_name = result
            return model.Facilities(facility_id, facility_name)
        else:
            return None
    
    def update_facilities_name(self, facility_name: str) -> model.Facilities:
        if facilities is None:
            raise ValueError("Facilities Name cannot be None")

        sql = """
        UPDATE Facilities SET facility_name = ? WHERE facility_id = ?
        """
        params = tuple([facility_name, facility_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_facilities(self, facility_id: int) -> model.Facilities:
        if facilities is None:
            raise ValueError("Facilities cannot be None")

        sql = """
        DELETE FROM Facilities WHERE facility_id = ?
        """
        params = tuple([facility_id])
        last_row_id, row_count = self.execute(sql, params)

    def read_facilities_by_roomtype_id(self, type_id: int) -> model.Facility
        sql = """
        SELECT Facility.name FROM Facility JOIN RoomtypeFacility ON Facility.facility_id = RoomtypeFacility.facility_id
        WHERE RoomtypeFacility.roomtype_id = ?;
        """
        params = (type_id,)
        results = self.fetchall(sql, params)
        facilities = []
        for row in results:
        facility_name = row[0]
        facilities.append(facility_name)
        return facilities

    def insert_facility(self, name: str) -> model.Facility
        sql = """
        "INSERT INTO Facilities (name) VALUES (?)"
        """
        return self.execute(sql, (name,))[0]