from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
    
    def create_new_address(self, street:str, city:str, zip_code:int) -> model.Address:
        if street is None:
            raise ValueError ("Street is required")
        if city is None:
            raise ValueError ("City is required")
        if zip_code is None:
            raise ValueError ("Zip Code is required")
            
        sql = """
        INSERT INTO Address (Street, City, Zip_code) VALUES (?, ?, ?)
        """

        params = tuple([street, city, zip_code])

        last_row_id, row_count = self.execute(sql, params)
        return model.Address(last_row_id, street, city, zip_code)

    def read_address_by_city(self, city: str, hotel: model.Hotel) -> model.Address:
        
        sql = """
        SELECT Address_Id, Street, City, Zip_code FROM Hotel WHERE city = ?
        """
        if city is None:
            raise ValueError("City can not be None")
        if hotel is None:
            raise ValueError("Hotel can not be None")

        params = tuple([city.hotel_id])
        address = self.fetchall(sql, params)
        return [model.Address(Address_Id, street, city, zip_code) for Address_Id, city in address]