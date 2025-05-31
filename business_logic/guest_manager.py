import os

import model
import data_access

class GuestManager:
    def __init__(self):
        self.__guest_da = data_access.GuestDataAccess()

    def create_guest(self, first_name: str, last_name: str, email: str, address: model.Address = None) -> model.Guest:
        return self.__guest_da.create_new_guest(first_name, last_name, email, address)

    def read_guest(self, guest_id: int) -> model.Guest:
        return self.__guest_da.read_guest_by_id(guest_id)

    def read_guest_by_email(self, email: str) -> model.Guest:
        return self.__guest_da.read_guest_by_email(email)

    def read_all_guests(self) -> list[model.Guest]:
        return self.__guest_da.read_all_guests()

    def update_guest(self, guest: model.Guest) -> None:
        self.__guest_da.update_guest(guest)

    def delete_guest(self, guest: model.Guest) -> None:
        self.__guest_da.delete_guest(guest)