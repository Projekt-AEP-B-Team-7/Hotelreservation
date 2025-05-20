import os

import model
import data_access

class GuestManager:
    def __init__(self) -> None:
        self.__guest_dal = data_access.guestDataAccess()

    def create_guest(self, guest_id:int, room_id:int, check_in_date:str, check_out_date:str, is_cancelled:bool, total_amount: float) -> model.Guest:
        return self.__guest_dal.create_new_guest(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)

    def read_all_guests(self, first_name, last_name, email, address_id) -> model.Guest:
        return self.__guest_dal.read_all_guests(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)

    def update_guest_name(self, : bool) -> model.Guest:
        return self.__guest_dal.update_guest_name(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)

    def delete_guest(self, guest_id) -> model.Guest:
        return self.__guest_dal.delete_guest(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)