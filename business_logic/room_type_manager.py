import os

import model
import data_access

class RoomtypeManager:
    def __init__(self) -> None:
        self.__roomtype_dal = data_access.RoomtypeDataAccess()

    def read_roomtype_by_hotel_id(self, hotel_id: int) -> model.Roomtype:
        return self.__roomtype_dal.read_roomtype_by_id(type_id)

    def update_roomtype(self, type_id: int) -> model.Roomtype:
        return self.__roomtype_dal.update_roomtype(type_id)

    def delete_roomtype(self, type_id: int) -> model.Roomtype:
        return self.__roomtype_dal.delete_roomtype(type_id)

    #def insert_roomtype(self, type_id: int) -> model.Roomtype:
        return self.__roomtype_dal.insert_roomtype(type_id)