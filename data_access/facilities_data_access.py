from __future__ import annotations
import model
from model.facilities import Facilities
from data_access.base_data_access import BaseDataAccess

class FacilitiesDataAccess(BaseDataAccess):
    
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # User Story 10: Facilities erstellen
    def create_new_facility(self, facility_name: str) -> Facilities:
        if not facility_name:
            raise ValueError("Facility name is required")
        
        sql = """
        INSERT INTO Facilities (Facility_name) VALUES (?)
        """
        params = tuple([facility_name])
        last_row_id, row_count = self.execute(sql, params)
        return Facilities(last_row_id, facility_name)

    def read_facility_by_id(self, facility_id: int) -> Facilities | None:
        sql = """
        SELECT Facility_id, Facility_name FROM Facilities WHERE Facility_id = ?
        """
        params = tuple([facility_id])
        result = self.fetchone(sql, params)
        if result:
            facility_id, facility_name = result
            return Facilities(facility_id, facility_name)
        return None

    def read_facility_by_name(self, facility_name: str) -> Facilities | None:
        sql = """
        SELECT Facility_id, Facility_name FROM Facilities WHERE Facility_name = ?
        """
        params = tuple([facility_name])
        result = self.fetchone(sql, params)
        if result:
            facility_id, facility_name = result
            return Facilities(facility_id, facility_name)
        return None

    # User Story 9: Alle Facilities für Admin
    def read_all_facilities(self) -> list[Facilities]:
        sql = """
        SELECT Facility_id, Facility_name FROM Facilities ORDER BY Facility_name
        """
        result = self.fetchall(sql, tuple())
        return [
            Facilities(facility_id, facility_name) 
            for facility_id, facility_name in result
        ]

    # User Story 2.1: Facilities nach Zimmertyp
    def read_facilities_by_room_type_id(self, type_id: int) -> list[Facilities]:
        sql = """
        SELECT f.Facility_id, f.Facility_name 
        FROM Facilities f 
        JOIN Room_Type_Facilities rtf ON f.Facility_id = rtf.Facility_id
        WHERE rtf.Type_id = ?
        ORDER BY f.Facility_name
        """
        params = tuple([type_id])
        result = self.fetchall(sql, params)
        return [
            Facilities(facility_id, facility_name) 
            for facility_id, facility_name in result
        ]

    # User Story 2.1: Facilities nach Room ID
    def read_facilities_by_room_id(self, room_id: int) -> list[Facilities]:
        sql = """
        SELECT f.Facility_id, f.Facility_name 
        FROM Facilities f 
        JOIN Room_Type_Facilities rtf ON f.Facility_id = rtf.Facility_id
        JOIN Room r ON rtf.Type_id = r.Type_id
        WHERE r.Room_id = ?
        ORDER BY f.Facility_name
        """
        params = tuple([room_id])
        result = self.fetchall(sql, params)
        return [
            Facilities(facility_id, facility_name) 
            for facility_id, facility_name in result
        ]

    # User Story 2.1: Facilities suchen
    def search_facilities(self, search_term: str) -> list[Facilities]:
        sql = """
        SELECT Facility_id, Facility_name 
        FROM Facilities 
        WHERE Facility_name LIKE ?
        ORDER BY Facility_name
        """
        params = tuple([f"%{search_term}%"])
        result = self.fetchall(sql, params)
        return [
            Facilities(facility_id, facility_name) 
            for facility_id, facility_name in result
        ]

    # User Story 10: Facility aktualisieren
    def update_facility(self, facility_id: int, facility_name: str) -> bool:
        if not facility_name:
            raise ValueError("Facility name cannot be empty")

        sql = """
        UPDATE Facilities SET Facility_name = ? WHERE Facility_id = ?
        """
        params = tuple([facility_name, facility_id])
        last_row_id, row_count = self.execute(sql, params)
        return row_count > 0

    # User Story 10: Facility löschen
    def delete_facility(self, facility_id: int) -> bool:
        sql = """
        DELETE FROM Facilities WHERE Facility_id = ?
        """
        params = tuple([facility_id])
        last_row_id, row_count = self.execute(sql, params)
        return row_count > 0

    # Hilfsmethoden für Room-Type-Facility Verknüpfungen
    def add_facility_to_room_type(self, room_type_id: int, facility_id: int) -> bool:
        """User Story 10: Facility zu Zimmertyp hinzufügen"""
        sql = """
        INSERT INTO Room_Type_Facilities (Type_id, Facility_id) VALUES (?, ?)
        """
        params = tuple([room_type_id, facility_id])
        try:
            last_row_id, row_count = self.execute(sql, params)
            return row_count > 0
        except:
            return False  # Bereits vorhanden oder Fehler

    def remove_facility_from_room_type(self, room_type_id: int, facility_id: int) -> bool:
        """User Story 10: Facility von Zimmertyp entfernen"""
        sql = """
        DELETE FROM Room_Type_Facilities WHERE Type_id = ? AND Facility_id = ?
        """
        params = tuple([room_type_id, facility_id])
        last_row_id, row_count = self.execute(sql, params)
        return row_count > 0