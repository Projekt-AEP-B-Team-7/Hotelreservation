from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
    
    def create_new_guest(self, first_name:str, last_name:str, email:str) -> model.Guest:
        if first_name is None:
            raise ValueError ("First Name is required")
        if last_name is None:
            raise ValueError ("Last Name is required")
        if email is None:
            raise ValueError ("Email is required")
        if check_out_date is None:
        

        sql = """
        INSERT INTO Guest (first_name, last_name, email) VALUES (?, ?, ?)
        """

        params = tuple([first_name, last_name, email])

        last_row_id, row_count = self.execute(sql, params)
        return model.Guest(last_row_id, first_name, last_name, email)

    #def read_guest_by_(self, city: str, hotel: model.Hotel) -> model.Guest:
     #   sql = """
     #   SELECT Address_Id, Street, City, Zip_code FROM Hotel WHERE city = ?
     #   """
     #   if city is None:
     #       raise ValueError("City can not be None")
     #   if hotel is None:
     #       raise ValueError("Hotel can not be None")

#        params = tuple([city.hotel_id])
 #       address = self.fetchall(sql, params)
  #      return [model.Address(Address_Id, street, city, zip_code) for Address_Id, city in address]