from model.room_type import RoomType
from model.hotel import Hotel
from model.booking import Booking
from model.facilities import Facilities
from model.address import Address
from model.guest import Guest
from model.room import Room
from model.invoice import Invoice

from data_access.address_data_access import AddressDataAccess

class AddressManager:
    def __init__(self):
        self.__address_da = AddressDataAccess()

    def create_address(self, street: str, city: str, zip_code: str) -> Address:
        return self.__address_da.create_new_address(street, city, zip_code)

    def read_address(self, address_id: int) -> Address:
        return self.__address_da.read_address_by_id(address_id)

    def read_addresses_by_city(self, city: str) -> list[Address]:
        return self.__address_da.read_addresses_by_city(city)

    def read_all_addresses(self) -> list[Address]:
        return self.__address_da.read_all_addresses()

    def update_address(self, address: Address) -> None:
        self.__address_da.update_address(address)

    def delete_address(self, address: Address) -> None:
        self.__address_da.delete_address(address)