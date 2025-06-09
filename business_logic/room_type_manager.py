import os

from model.room_type import RoomType
from model.hotel import Hotel
from model.booking import Booking
from model.facilities import Facilities
from model.address import Address
from model.guest import Guest
from model.room import Room
from model.invoice import Invoice

from data_access.room_type_data_access import RoomTypeDataAccess

class RoomTypeManager:
    def __init__(self):
        self.__room_type_da = RoomTypeDataAccess()

    def create_room_type(self, description: str, max_guests: int) -> RoomType:
        return self.__room_type_da.create_room_type(description, max_guests)

    def read_roomtype_by_id(self, type_id: int) -> RoomType:
        return self.__room_type_da.read_roomtype_by_id(type_id)

    def read_room_type_by_description(self, description: str) -> RoomType:
        return self.__room_type_da.read_room_type_by_description(description)

    def read_all_room_types(self) -> list[RoomType]:
        return self.__room_type_da.read_all_room_types()

    def read_room_types_by_guest_capacity(self, min_guests: int) -> list[RoomType]:
        return self.__room_type_da.read_room_types_by_guest_capacity(min_guests)

    def update_room_type(self, room_type: RoomType) -> None:
        self.__room_type_da.update_room_type(room_type)

    def delete_room_type(self, room_type: RoomType) -> None:
        self.__room_type_da.delete_room_type(room_type)