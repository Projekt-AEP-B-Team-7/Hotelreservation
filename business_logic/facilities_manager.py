import model
from model.room_type import RoomType
from model.hotel import Hotel
from model.booking import Booking
from model.facilities import Facilities
from model.address import Address
from model.guest import Guest
from model.room import Room
from model.invoice import Invoice
from data_access.facilities_data_access import FacilitiesDataAccess

class FacilitiesManager:
    def __init__(self):
        self.__facilities_da = FacilitiesDataAccess()

    def create_facility(self, facility_name: str) -> Facilities:
        return self.__facilities_da.create_new_facility(facility_name)

    def read_facility(self, facility_id: int) -> Facilities:
        return self.__facilities_da.read_facility_by_id(facility_id)

    def read_facility_by_name(self, facility_name: str) -> Facilities:
        return self.__facilities_da.read_facility_by_name(facility_name)

    def read_all_facilities(self) -> list[Facilities]:
        return self.__facilities_da.read_all_facilities()

    def read_facilities_by_room(self, room: Room) -> list[Facilities]:
        return self.__facilities_da.read_facilities_by_room(room)

    def read_facilities_like_name(self, facility_name: str) -> list[Facilities]:
        return self.__facilities_da.read_facilities_like_name(facility_name)

    def add_facility_to_room(self, room: Room, facility: Facilities) -> None:
        self.__facilities_da.add_facility_to_room(room, facility)

    def remove_facility_from_room(self, room: Room, facility: Facilities) -> None:
        self.__facilities_da.remove_facility_from_room(room, facility)

    def update_facility(self, facility: Facilities) -> None:
        self.__facilities_da.update_facility(facility)

    def delete_facility(self, facility: Facilities) -> None:
        self.__facilities_da.delete_facility(facility)