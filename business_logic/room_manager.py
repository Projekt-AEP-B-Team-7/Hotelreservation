import os

from model.room import Room
import data_access

class RoomManager:
    def __init__(self):
        self.__room_da = data_access.RoomDataAccess()

    def create_room(self, hotel: model.Hotel, room_number: str, room_type: model.RoomType, price_per_night: float) -> model.Room:
        return self.__room_da.create_new_room(hotel, room_number, room_type, price_per_night)

    def read_room(self, room_id: int) -> model.Room:
        return self.__room_da.read_room_by_id(room_id)

    def read_rooms_by_hotel(self, hotel: model.Hotel) -> list[model.Room]:
        return self.__room_da.read_rooms_by_hotel(hotel)

    def read_rooms_by_type_and_hotel(self, hotel: model.Hotel, room_type: model.RoomType) -> list[model.Room]:
        return self.__room_da.read_rooms_by_type_and_hotel(hotel, room_type)

    def read_available_rooms_by_hotel(self, hotel: model.Hotel, check_in_date: str, check_out_date: str) -> list[model.Room]:
        return self.__room_da.read_available_rooms_by_hotel(hotel, check_in_date, check_out_date)

    def read_rooms_with_facilities(self, room: model.Room) -> list[model.Facilities]:
        return self.__room_da.read_rooms_with_facilities(room)

    def update_room(self, room: model.Room) -> None:
        self.__room_da.update_room(room)

    def delete_room(self, room: model.Room) -> None:
        self.__room_da.delete_room(room)
    
   