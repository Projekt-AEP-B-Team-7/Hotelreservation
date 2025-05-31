from __future__ import annotations
from model.guest import Guest
from data_access.base_data_access import BaseDataAccess

class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_guest(self, first_name: str, last_name: str, email: str, address: model.Address = None) -> Guest:
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
        return model.Guest(last_row_id, first_name, last_name, email, address)

    def read_guest_by_id(self, guest_id: int) -> Guest | None:
        if guest_id is None:
            raise ValueError("Guest ID is required")

        sql = """
        SELECT Guest.guest_id, Guest.first_name, Guest.last_name, Guest.email,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Guest g
        LEFT JOIN Address a ON g.address_id = a.address_id
        WHERE g.guest_id = ?
        """
        params = tuple([guest_id])
        result = self.fetchone(sql, params)
        if result:
            guest_id, first_name, last_name, email, address_id, street, city, zip_code = result
            address = None
            if address_id:
                address = model.Address(address_id, street, city, zip_code)
            return model.Guest(guest_id, first_name, last_name, email, address)
        else:
            return None

    def read_guest_by_email(self, email: str) -> model.Guest | None:
        if email is None:
            raise ValueError("Email is required")

        sql = """
        SELECT g.guest_id, g.first_name, g.last_name, g.email,
               a.address_id, a.street, a.city, a.zip_code
        FROM Guest g
        LEFT JOIN Address a ON g.address_id = a.address_id
        WHERE g.email = ?
        """
        params = tuple([email])
        result = self.fetchone(sql, params)
        if result:
            guest_id, first_name, last_name, email, address_id, street, city, zip_code = result
            address = None
            if address_id:
                address = model.Address(address_id, street, city, zip_code)
            return model.Guest(guest_id, first_name, last_name, email, address)
        else:
            return None

    def read_all_guests(self) -> list[model.Guest]:
        sql = """
        SELECT g.guest_id, g.first_name, g.last_name, g.email,
               a.address_id, a.street, a.city, a.zip_code
        FROM Guest g
        LEFT JOIN Address a ON g.address_id = a.address_id
        ORDER BY g.last_name, g.first_name
        """
        guests = self.fetchall(sql)
        
        return [
            model.Guest(
                guest_id,
                first_name,
                last_name,
                email,
                model.Address(address_id, street, city, zip_code) if address_id else None
            )
            for guest_id, first_name, last_name, email, address_id, street, city, zip_code in guests
        ]

    def read_guests_like_name(self, name: str) -> list[model.Guest]:
        if name is None:
            raise ValueError("Name is required")

        sql = """
        SELECT g.guest_id, g.first_name, g.last_name, g.email,
               a.address_id, a.street, a.city, a.zip_code
        FROM Guest g
        LEFT JOIN Address a ON g.address_id = a.address_id
        WHERE g.first_name LIKE ? OR g.last_name LIKE ?
        ORDER BY g.last_name, g.first_name
        """
        params = tuple([f"%{name}%", f"%{name}%"])
        guests = self.fetchall(sql, params)
        
        return [
            model.Guest(
                guest_id,
                first_name,
                last_name,
                email,
                model.Address(address_id, street, city, zip_code) if address_id else None
            )
            for guest_id, first_name, last_name, email, address_id, street, city, zip_code in guests
        ]

    def read_guests_with_bookings(self) -> list[model.Guest]:
        sql = """
        SELECT DISTINCT g.guest_id, g.first_name, g.last_name, g.email,
               a.address_id, a.street, a.city, a.zip_code
        FROM Guest g
        LEFT JOIN Address a ON g.address_id = a.address_id
        JOIN Booking b ON g.guest_id = b.guest_id
        WHERE b.is_cancelled = 0
        ORDER BY g.last_name, g.first_name
        """
        guests = self.fetchall(sql)
        
        return [
            model.Guest(
                guest_id,
                first_name,
                last_name,
                email,
                model.Address(address_id, street, city, zip_code) if address_id else None
            )
            for guest_id, first_name, last_name, email, address_id, street, city, zip_code in guests
        ]

    def update_guest(self, guest: model.Guest) -> None:
        if guest is None:
            raise ValueError("Guest cannot be None")

        sql = """
        UPDATE Guest SET first_name = ?, last_name = ?, email = ?, address_id = ? 
        WHERE guest_id = ?
        """
        params = tuple([
            guest.first_name,
            guest.last_name,
            guest.email,
            guest.address.address_id if guest.address else None,
            guest.guest_id
        ])
        last_row_id, row_count = self.execute(sql, params)

    def delete_guest(self, guest: model.Guest) -> None:
        if guest is None:
            raise ValueError("Guest cannot be None")

        sql = """
        DELETE FROM Guest WHERE guest_id = ?
        """
        params = tuple([guest.guest_id])
        last_row_id, row_count = self.execute(sql, params)