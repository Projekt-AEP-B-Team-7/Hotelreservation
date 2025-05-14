import os

import model
import data_access

class GuestManager:
    def __init__(self) -> None:
        self.__guest_dal = data_access.guestDataAccess()

    def create_new_guest(self, guest_id:int, room_id:int, check_in_date:str, check_out_date:str, is_cancelled:bool, total_amount: float) -> model.guest:
        guest = self.__guest_dal.create_new_guest(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        return guest