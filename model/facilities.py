from __future__ import annotations

class Facilities: 
    def __init__(self, facility_id: int, facility_name: str):
        if not facility_id:
            raise ValueError("Facility Id is required")
        if not isinstance(facility_id, int):
            raise ValueError("Facility Id must be an integer")
        if not facility_name:
            raise ValueError("Facility name is required")
        if not isinstance(facility_name, str):
            raise ValueError("Facility name must be a string")

        self.__facility_id: int = facility_id
        self.__facility_name: str = facility_name

    def __repr__(self):
        return f"Facilities(id={self.__facility_id!r}, Facility Name={self.__facility_name!r})"

    @property
    def facility_id(self) -> int:
        return self.__facility_id

    @property
    def facility_name(self) -> str:
        return self.__facility_name

    @facility_name.setter
    def facility_name(self, facility_name: str) -> None:
        if not facility_name:
            raise ValueError("Facility name is required")
        if not isinstance(facility_name, str):
            raise ValueError("Facility name must be a string")
        self.__facility_name = facility_name