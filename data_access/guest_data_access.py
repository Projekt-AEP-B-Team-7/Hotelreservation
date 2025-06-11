import model

from model.room_type import RoomType
from model.hotel import Hotel
from model.booking import Booking
from model.facilities import Facilities
from model.address import Address
from model.guest import Guest
from model.room import Room
from model.invoice import Invoice
from data_access.base_data_access import BaseDataAccess

class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_guest(self, first_name: str, last_name: str, email: str, address: Address = None) -> Guest:
        if first_name is None:
            raise ValueError("First name is required")
        if last_name is None:
            raise ValueError("Last name is required")
        if email is None:
            raise ValueError("Email is required")

        sql = """
        INSERT INTO Guest (first_name, last_name, email, address_id) VALUES (?, ?, ?, ?)
        """
        params = (first_name, last_name, email,
            address.address_id if address else None,)
        last_row_id, row_count = self.execute(sql, params)
        return Guest(last_row_id, first_name, last_name, email, address)

    def read_all_guests_w_phone_number(self) -> list[Guest]:
        sql = """
        SELECT Guest.guest_id, Guest.first_name, Guest.last_name, Guest.email, Guest.phone_number,
            Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Guest
        LEFT JOIN Address ON Guest.address_id = Address.address_id
        ORDER BY Guest.last_name, Guest.first_name
        """
        guests = self.fetchall(sql)
        
        return [Guest(guest_id, first_name, last_name, email, phone_number,
                Address(address_id, street, city, zip_code) if address_id else None)
            for guest_id, first_name, last_name, email, phone_number, address_id, street, city, zip_code in guests]

    def read_guest_by_id(self, guest_id: int) -> Guest | None:
        if guest_id is None:
            raise ValueError("Guest ID is required")

        sql = """
        SELECT Guest.guest_id, Guest.first_name, Guest.last_name, Guest.email,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Guest
        LEFT JOIN Address ON Guest.address_id = Address.address_id
        WHERE Guest.guest_id = ?
        """
        params = tuple([guest_id])
        result = self.fetchone(sql, params)
        if result:
            guest_id, first_name, last_name, email, address_id, street, city, zip_code = result
            address = None
            if address_id:
                address = Address(address_id, street, city, zip_code)
            return Guest(guest_id, first_name, last_name, email, address)
        else:
            return None

    def read_guest_by_email(self, email: str) -> Guest | None:
        if email is None:
            raise ValueError("Email is required")

        sql = """
        SELECT Guest.guest_id, Guest.first_name, Guest.last_name, Guest.email,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Guest
        LEFT JOIN Address ON Guest.address_id = Address.address_id
        WHERE Guest.email = ?
        """
        params = tuple([email])
        result = self.fetchone(sql, params)
        if result:
            guest_id, first_name, last_name, email, address_id, street, city, zip_code = result
            address = None
            if address_id:
                address = Address(address_id, street, city, zip_code)
            return Guest(guest_id, first_name, last_name, email, address)
        else:
            return None

    def read_all_guests(self) -> list[Guest]:
        sql = """
        SELECT Guest.guest_id, Guest.first_name, Guest.last_name, Guest.email,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Guest
        LEFT JOIN Address ON Guest.address_id = Address.address_id
        ORDER BY Guest.last_name, Guest.first_name
        """
        guests = self.fetchall(sql)
        
        return [Guest(guest_id, first_name, last_name, email,
                Address(address_id, street, city, zip_code) if address_id else None)
            for guest_id, first_name, last_name, email, address_id, street, city, zip_code in guests]

    def read_guests_like_name(self, name: str) -> list[Guest]:
        if name is None:
            raise ValueError("Name is required")

        sql = """
        SELECT Guest.guest_id, Guest.first_name, Guest.last_name, Guest.email,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Guest
        LEFT JOIN Address ON Guest.address_id = Address.address_id
        WHERE Guest.first_name LIKE ? OR Guest.last_name LIKE ?
        ORDER BY Guest.last_name, Guest.first_name
        """
        params = tuple([f"%{name}%", f"%{name}%"])
        guests = self.fetchall(sql, params)
        
        return [Guest(guest_id, first_name, last_name, email,
                Address(address_id, street, city, zip_code) if address_id else None)
            for guest_id, first_name, last_name, email, address_id, street, city, zip_code in guests]

    def read_guests_with_bookings(self) -> list[Guest]:
        sql = """
        SELECT DISTINCT Guest.guest_id, Guest.first_name, Guest.last_name, Guest.email,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Guest
        LEFT JOIN Address ON Guest.address_id = Address.address_id
        JOIN Booking ON Guest.guest_id = Booking.guest_id
        WHERE Booking.is_cancelled = 0
        ORDER BY Guest.last_name, Guest.first_name
        """
        guests = self.fetchall(sql)
        
        return [Guest(guest_id, first_name, last_name, email,
                Address(address_id, street, city, zip_code) if address_id else None)
            for guest_id, first_name, last_name, email, address_id, street, city, zip_code in guests]

    def update_guest(self, guest: Guest) -> None:
        if guest is None:
            raise ValueError("Guest cannot be None")

        sql = """
        UPDATE Guest SET first_name = ?, last_name = ?, email = ?, address_id = ? 
        WHERE guest_id = ?
        """
        params = tuple([guest.first_name, guest.last_name, guest.email,
            guest.address.address_id if guest.address else None, guest.guest_id])
        last_row_id, row_count = self.execute (sql, params)

    def read_all_guests_w_phone_number(self) -> list[Guest]:
        sql = """
        SELECT Guest.guest_id, Guest.first_name, Guest.last_name, Guest.email, Guest.phone_number,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Guest
        LEFT JOIN Address ON Guest.address_id = Address.address_id
        ORDER BY Guest.last_name, Guest.first_name
        """
        return [Guest(guest_id, first_name, last_name, email, phone_number,
                Address(address_id, street, city, zip_code) if address_id else None)
            for guest_id, first_name, last_name, email, phone_number, address_id, street, city, zip_code in guests]

    
    def update_guest_phone(self, guest_id: int, new_phone: str) -> bool:
        sql = "UPDATE Guest SET phone_number = ? WHERE guest_id = ?"
        params = tuple([guest_id, new_phone])
        last_row_id, row_count = self.execute (sql, params)
        return row_count > 0 

    def delete_guest(self, guest: Guest) -> None:
        if guest is None:
            raise ValueError ("Guest cannot be None")
        sql = """
        DELETE FROM Guest WHERE guest_id = ?
        """
        params = tuple([guest.guest_id])
        last_row_id, row_count = self.execute(sql, params)