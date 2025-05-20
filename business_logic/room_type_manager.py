import model
import data_access

class RoomtypeManager:
    def __init__(self) -> None:
        self.__roomtype_dal = data_access.RoomtypeDataAccess()

    def read_roomtypes_by_hotel_id(self, hotel_id: int) -> model.Roomtype
        return self.__roomtype_dal.read_roomtypes_by_hotel_id(hotel_id)

    def update_roomtype_price(self, type_id: int, new_price: float) -> model.Roomtype
        return self.__roomtype_dal.update_roomtype_price(type_id, new_price)

    def delete_roomtype(self, type_id: int) -> model.Roomtype:
        return self.__roomtype_dal.delete_roomtype(type_id)
