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
    