import os

import model
import data_access

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_dal = data_access.HotelDataAccess()

    def read_hotel_by_name(self, name: str) -> model.Hotel:
        hotel = self.__hotel_dal.read_hotel_by_name(name)
        return hotel