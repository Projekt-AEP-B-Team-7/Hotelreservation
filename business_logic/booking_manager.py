import os

import model
import data_access

class BookingManager:
    def __init__(self) -> None:
        self.__booking_dal = data_access.BookingDataAccess()

    def create_booking(self, guest_id:int, room_id:int, check_in_date:str, check_out_date:str, is_cancelled:bool, total_amount: float) -> model.Booking:
        return self.__booking_dal.create_new_booking(name)
    
    def read_booking_guestId(self, city: str, hotel: model.Hotel) -> model.Booking:
        return self.__booking_dal.read_booking_by_guestId()
    
    def update_booking(self, is_cancelled: bool) -> model.Booking:
        return self.__booking_dal.update_booking(is_cancelled)
    
    def delete_booking(self, booking_id) -> model.Booking:
        return self.__booking_dal.delete_booking(booking_id)