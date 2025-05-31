import model
from model.facilities import Facilities
from data_access.facilities_data_access import FacilitiesDataAccess

class FacilitiesManager:
    def __init__(self) -> None:
        self.__facilities_dal = FacilitiesDataAccess()

    # User Story 10: Facility erstellen
    def create_facility(self, facility_name: str) -> Facilities:
        return self.__facilities_dal.create_new_facility(facility_name)

    # Read-Methoden
    def read_facility_by_id(self, facility_id: int) -> Facilities | None:
        return self.__facilities_dal.read_facility_by_id(facility_id)
    
    def read_facility_by_name(self, facility_name: str) -> Facilities | None:
        return self.__facilities_dal.read_facility_by_name(facility_name)

    # User Story 9: Alle Facilities für Admin
    def get_all_facilities(self) -> list[Facilities]:
        return self.__facilities_dal.read_all_facilities()

    # User Story 2.1: Facilities für Zimmerdetails
    def get_facilities_by_room_type(self, type_id: int) -> list[Facilities]:
        return self.__facilities_dal.read_facilities_by_room_type_id(type_id)

    def get_facilities_by_room(self, room_id: int) -> list[Facilities]:
        return self.__facilities_dal.read_facilities_by_room_id(room_id)

    # User Story 2.1: Facilities suchen
    def search_facilities(self, search_term: str) -> list[Facilities]:
        if not search_term or len(search_term.strip()) < 2:
            return []
        return self.__facilities_dal.search_facilities(search_term.strip())

    # User Story 10: Facility aktualisieren
    def update_facility(self, facility_id: int, facility_name: str) -> bool:
        return self.__facilities_dal.update_facility(facility_id, facility_name)

    # User Story 10: Facility löschen
    def delete_facility(self, facility_id: int) -> bool:
        return self.__facilities_dal.delete_facility(facility_id)

    # User Story 10: Facilities zu Zimmertypen verwalten
    def add_facility_to_room_type(self, room_type_id: int, facility_id: int) -> bool:
        return self.__facilities_dal.add_facility_to_room_type(room_type_id, facility_id)

    def remove_facility_from_room_type(self, room_type_id: int, facility_id: int) -> bool:
        return self.__facilities_dal.remove_facility_from_room_type(room_type_id, facility_id)

    # User Story 2.1: Facility-Namen für Zimmer abrufen
    def get_facility_names_by_room(self, room_id: int) -> list[str]:
        facilities = self.get_facilities_by_room(room_id)
        return [facility.facility_name for facility in facilities]

    def get_facility_names_by_room_type(self, type_id: int) -> list[str]:
        facilities = self.get_facilities_by_room_type(type_id)
        return [facility.facility_name for facility in facilities]

    # User Story 9: Facility-Übersicht für Admin
    def get_facilities_summary(self) -> dict:
        """Übersicht aller Facilities mit Anzahl verwendender Zimmertypen"""
        facilities = self.get_all_facilities()
        summary = {}
        
        for facility in facilities:
            # Zähle wie viele Zimmertypen diese Facility verwenden
            # TODO: Implementierung mit Room_Type_Facilities Join
            summary[facility.facility_name] = {
                'id': facility.facility_id,
                'name': facility.facility_name,
                'usage_count': 0  # Platzhalter
            }
        
        return summary

# Standard-Facilities erstellen
def create_default_facilities(manager: FacilitiesManager):
    """User Story 2.1: Standard-Ausstattung für Hotels"""
    default_facilities = [
        "WiFi", "TV", "Minibar", "Safe", "Klimaanlage", 
        "Balkon", "Badewanne", "Föhn", "Telefon", "Room Service"
    ]
    
    for facility_name in default_facilities:
        try:
            existing = manager.read_facility_by_name(facility_name)
            if not existing:
                manager.create_facility(facility_name)
                print(f"Standard facility '{facility_name}' created.")
        except Exception as e:
            print(f"Error creating facility '{facility_name}': {e}")