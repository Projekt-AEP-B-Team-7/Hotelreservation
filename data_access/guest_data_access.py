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

    def read_all_guests(self, first_name, last_name, email, address_id) -> model.Guest:
        
        sql = """
        SELECT * FROM Guest
        """
        params = tuple([first_name, last_name, email, address_id])
        result = self.fetchone(sql, params)
        return model.Guest(last_row_id, first_name, last_name, email)
    
   # def update_guest(self, is_cancelled: bool) -> model.Guest:
   #     if guest is None:
    #        raise ValueError("Guest cannot be None")

    #    sql = """
    #    UPDATE Guest SET first_name = ? WHERE guest_id = ?
    #    """
    #    params = tuple([is_cancelled, booking_id])
    #    last_row_id, row_count = self.execute(sql, params)

  #  def delete_guest(self, booking_id) -> model.Guest:
    #    if guest is None:
    #        raise ValueError("Booking cannot be None")

 #     sql = """
   #     DELETE FROM Guest WHERE booking_id = ?
    #    """
    #    params = tuple([booking_id])
    #    last_row_id, row_count = self.execute(sql, params)