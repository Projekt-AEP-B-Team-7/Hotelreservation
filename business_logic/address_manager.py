import os

import model
import data_access

class AddressManager:
    def __init__(self) -> None:
        self.__address_dal = data_access.AddressDataAccess()

    def create_address(self, street:str, city:str, zip_code:int) -> model.Address:
        return self.__address_dal.create_new_address(street, city, zip_code)
    
    def read_address_city(self, city: str, hotel: model.Hotel) -> model.Address:
        return self.__address_dal.read_address_by_city(city)