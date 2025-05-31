import os

from model.room import Room
import data_access

class RoomManager:
    def __init__(self) -> None:
        self.__room_dal = data_access.RoomDataAccess()

    def read_room_by_hotel_id(self, hotel_id: int) -> model.Room:
        return self.__room_dal.read_room_by_hotel_id(room_id, hotel_id, room_number, type_id, price_per_night)
    
    def update_room_price(self, room_id: int) -> model.Room:
        return self.__room_dal.update_room_price(room_id)
    
    def delete_room(self, room_id: int) -> model.Room:
        return self.__room_dal.delete_room(room_id)

    def get_available_rooms(self, city: str, max_guests: int, check_in: str, check_out: str) -> list[Hotel]:
        return self.__room_dal.get_available_rooms(city, max_guests, check_in, check_out)

    def get_all_rooms_with_facilities(self,room_id: int) -> model.Room
        return self.__room_dal.get_rooms_with_facilities()

    #def insert_room_price(self, room_id: int) -> model.Room:
        return self.__room_dal.insert_room_price(room_id)
    
   