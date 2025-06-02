import os

import model
from model.guest import Guest
from model.address import Address
import data_access
from data_access.guest_data_access import GuestDataAccess


class GuestManager:
    def __init__(self):
        self.__guest_da = GuestDataAccess()

    def create_guest(self, first_name: str, last_name: str, email: str, address: Address = None) -> Guest:
        return self.__guest_da.create_new_guest(first_name, last_name, email, address)

    def read_guest(self, guest_id: int) -> Guest:
        return self.__guest_da.read_guest_by_id(guest_id)

    def read_guest_by_email(self, email: str) -> Guest:
        return self.__guest_da.read_guest_by_email(email)

    def read_all_guests(self) -> list[Guest]:
        return self.__guest_da.read_all_guests()

    def update_guest(self, guest: Guest) -> None:
        self.__guest_da.update_guest(guest)

    def delete_guest(self, guest: Guest) -> None:
        self.__guest_da.delete_guest(guest)