from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
    
    def create_new_booking(self, guest_id:int, room_id:int, check_in_date:str, check_out_date:str, is_cancelled:bool, total_amount: float) -> model.Booking:
        if guest_id is None:
            raise ValueError ("Guest ID is required")
        if room_id is None:
            raise ValueError ("Room ID is required")
        if check_in_date is None:
            raise ValueError ("Check in date is required")
        if check_out_date is None:
            raise ValueError ("Check out date is required")
        if is_cancelled is None:
            raise ValueError ("Cancellation must be true or false")
        if total_amount is None:
            raise ValueError ("Total amount is required")            
    
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, total_amount) VALUES (?, ?, ?, ?, ?)
        """

        params = tuple([guest_id, room_id, check_in_date, check_out_date, total_amount])

        last_row_id, row_count = self.execute(sql, params)
        return model.Booking(last_row_id, guest_id, room_id, check_in_date, check_out_date, total_amount)

    def read_booking_by_guestId(self, city: str, hotel: model.Hotel) -> model.Booking:
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