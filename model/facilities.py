class Facilities:
    facilities_list = []  # Static list to manage all facilities

    def __init__(self, facility_id: int, facility_name: str):
        self._facility_id = facility_id
        self._facility_name = facility_name

    @property
    def facility_id(self) -> int:
        return self._facility_id

    @property
    def facility_name(self) -> str:
        return self._facility_name

    @classmethod
    def add_facility(cls, facility):
        """Adds a new facility to the list."""
        cls.facilities_list.append(facility)
        print(f"Facility '{facility.facility_name}' added.")

    @classmethod
    def remove_facility(cls, facility_id: int):
        """Removes a facility based on its ID."""
        for facility in cls.facilities_list:
            if facility.facility_id == facility_id:
                cls.facilities_list.remove(facility)
                print(f"Facility '{facility.facility_name}' removed.")
                return
        print(f"Facility with ID {facility_id} not found.") 
