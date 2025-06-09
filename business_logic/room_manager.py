import os
import model

from model.room_type import RoomType
from model.hotel import Hotel
from model.booking import Booking
from model.facilities import Facilities
from model.address import Address
from model.guest import Guest
from model.room import Room
from model.invoice import Invoice
from data_access.room_data_access import RoomDataAccess

class RoomManager:
    def __init__(self):
        self.__room_da = RoomDataAccess()

    def create_room(self, hotel: Hotel, room_number: str, room_type: RoomType, price_per_night: float) -> Room:
        return self.__room_da.create_new_room(hotel, room_number, room_type, price_per_night)

    def read_room(self, room_id: int) -> Room:
        return self.__room_da.read_room_by_id(room_id)

    def read_rooms_by_hotel(self, hotel: Hotel) -> list[Room]:
        return self.__room_da.read_rooms_by_hotel(hotel)

    def read_rooms_by_type_and_hotel(self, hotel: Hotel, room_type: RoomType) -> list[Room]:
        return self.__room_da.read_rooms_by_type_and_hotel(hotel, room_type)

    def read_available_rooms_by_hotel(self, hotel: Hotel, check_in_date: str, check_out_date: str) -> list[Room]:
        return self.__room_da.read_available_rooms_by_hotel(hotel, check_in_date, check_out_date)

    def read_all_rooms_with_facilities(self) -> list[Room]:
        return self.__room_da.read_rooms_with_facilities(room)

    def update_room(self, room: Room) -> None:
        self.__room_da.update_room(room)

    def delete_room(self, room: Room) -> None:
        self.__room_da.delete_room(room)
    
    def read_all_rooms_with_facilities(self) -> list[Room]:
        return self.__room_da.read_all_rooms_with_facilities()


    
   