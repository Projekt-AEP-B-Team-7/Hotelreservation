import os

import model
import data_access

class BookingManager:
    def __init__(self) -> None:
        self.__booking_dal = data_access.BookingDataAccess()

    def create_new_booking((self, guest_id:int, room_id:int, check_in_date:str, check_out_date:str, is_cancelled:bool, total_amount: float) -> model.Booking:
        booking = self.__booking_dal.create_new_booking(name)
        return booking