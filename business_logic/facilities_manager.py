import model
from model.facilities import Facilities
from data_access.facilities_data_access import FacilitiesDataAccess

class FacilitiesManager:
    def __init__(self):
        self.__facilities_da = data_access.FacilitiesDataAccess()

    def create_facility(self, facility_name: str) -> model.Facilities:
        return self.__facilities_da.create_new_facility(facility_name)

    def read_facility(self, facility_id: int) -> model.Facilities:
        return self.__facilities_da.read_facility_by_id(facility_id)

    def read_facility_by_name(self, facility_name: str) -> model.Facilities:
        return self.__facilities_da.read_facility_by_name(facility_name)

    def read_all_facilities(self) -> list[model.Facilities]:
        return self.__facilities_da.read_all_facilities()

    def read_facilities_by_room(self, room: model.Room) -> list[model.Facilities]:
        return self.__facilities_da.read_facilities_by_room(room)

    def read_facilities_like_name(self, facility_name: str) -> list[model.Facilities]:
        return self.__facilities_da.read_facilities_like_name(facility_name)

    def add_facility_to_room(self, room: model.Room, facility: model.Facilities) -> None:
        self.__facilities_da.add_facility_to_room(room, facility)

    def remove_facility_from_room(self, room: model.Room, facility: model.Facilities) -> None:
        self.__facilities_da.remove_facility_from_room(room, facility)

    def update_facility(self, facility: model.Facilities) -> None:
        self.__facilities_da.update_facility(facility)

    def delete_facility(self, facility: model.Facilities) -> None:
        self.__facilities_da.delete_facility(facility)