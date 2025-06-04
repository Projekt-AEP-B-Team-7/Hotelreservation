from __future__ import annotations
from model.room_type import RoomType
from model.hotel import Hotel
from model.booking import Booking
from model.facilities import Facilities
from model.address import Address
from model.guest import Guest
from model.room import Room
from model.invoice import Invoice
from data_access.base_data_access import BaseDataAccess

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_address(self, street: str, city: str, zip_code: str) -> Address:
        if street is None:
            raise ValueError("Street is required")
        if city is None:
            raise ValueError("City is required")
        if zip_code is None:
            raise ValueError("Zip code is required")

        sql = """
        INSERT INTO Address (street, city, zip_code) VALUES (?, ?, ?)
        """
        params = (street, city, zip_code)
        last_row_id, row_count = self.execute(sql, params)
        return Address(last_row_id, street, city, zip_code)

    def read_address_by_id(self, address_id: int) -> Address | None:
        if address_id is None:
            raise ValueError("Address ID is required")

        sql = """
        SELECT address_id, street, city, zip_code FROM Address WHERE address_id = ?
        """
        params = tuple([address_id])
        result = self.fetchone(sql, params)
        if result:
            address_id, street, city, zip_code = result
            return Address(address_id, street, city, zip_code)
        else:
            return None

    def read_addresses_by_city(self, city: str) -> list[Address]:
        if city is None:
            raise ValueError("City is required")

        sql = """
        SELECT address_id, street, city, zip_code FROM Address WHERE city = ?
        """
        params = tuple([city])
        addresses = self.fetchall(sql, params)
        return [
            Address(address_id, street, city, zip_code)
            for address_id, street, city, zip_code in addresses
        ]

    def read_all_addresses(self) -> list[Address]:
        sql = """
        SELECT address_id, street, city, zip_code FROM Address ORDER BY city, street
        """
        addresses = self.fetchall(sql)
        return [
            Address(address_id, street, city, zip_code)
            for address_id, street, city, zip_code in addresses
        ]

    def update_address(self, address: Address) -> None:
        if address is None:
            raise ValueError("Address cannot be None")

        sql = """
        UPDATE Address SET street = ?, city = ?, zip_code = ? WHERE address_id = ?
        """
        params = tuple([address.street, address.city, address.zip_code, address.address_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_address(self, address: Address) -> None:
        if address is None:
            raise ValueError("Address cannot be None")

        sql = """
        DELETE FROM Address WHERE address_id = ?
        """
        params = tuple([address.address_id])
        last_row_id, row_count = self.execute(sql, params)