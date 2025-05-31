from __future__ import annotations

class Facilities:
    def __init__(self, facility_id: int, facility_name: str):
        if facility_id is not None and not isinstance(facility_id, int):
            raise ValueError("facility_id must be an integer")
        if not facility_name:
            raise ValueError("facility_name is required")
        if not isinstance(facility_name, str):
            raise ValueError("facility_name must be a string")

        self.__facility_id: int = facility_id
        self.__facility_name: str = facility_name

    def __repr__(self):
        return f"Facilities(id={self.__facility_id!r}, name={self.__facility_name!r})"

    def __str__(self) -> str:
        return self.__facility_name

    @property
    def facility_id(self) -> int:
        return self.__facility_id

    @property
    def facility_name(self) -> str:
        return self.__facility_name

    @facility_name.setter
    def facility_name(self, facility_name: str) -> None:
        if not facility_name:
            raise ValueError("facility_name is required")
        if not isinstance(facility_name, str):
            raise ValueError("facility_name must be a string")
        self.__facility_name = facility_name

    # User Story Support Methods
    def matches_name(self, search_term: str) -> bool:
        """User Story 2.1: Facility-Suche"""
        if not search_term:
            return False
        return search_term.lower() in self.__facility_name.lower()