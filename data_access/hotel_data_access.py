from __future__ import annotations
from hotel.model import Hotel
from address.model import Address
from data_access.base_data_access import BaseDataAccess

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_hotel(self, name: str, stars: int, address: Address = None) -> Hotel:
        if name is None:
            raise ValueError("Hotel name is required")
        if stars is None:
            raise ValueError("Hotel stars is required")

        sql = """
        INSERT INTO Hotel (name, stars, address_id) VALUES (?, ?, ?)
        """
        params = (name, stars, address.address_id if address else None)
        last_row_id, row_count = self.execute(sql, params)
        return Hotel(last_row_id, name, stars, address)

    def read_hotel_by_id(self, hotel_id: int) -> Hotel | None:
        if hotel_id is None:
            raise ValueError("Hotel ID is required")

        sql = """
        SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        LEFT JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Hotel.hotel_id = ?
        """
        params = tuple([hotel_id])
        result = self.fetchone(sql, params)
        if result:
            hotel_id, name, stars, address_id, street, city, zip_code = result
            address = None
            if address_id:
                address = Address(address_id, street, city, zip_code)
            return Hotel(hotel_id, name, stars, address)
        else:
            return None

    def read_hotels_by_city(self, city: str) -> list[Hotel]:
        if city is None:
            raise ValueError("City cannot be None")

        sql = """
        SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Address.city = ?
        ORDER BY Hotel.stars DESC, Hotel.name
        """
        params = tuple([city])
        hotels = self.fetchall(sql, params)
        
        return [Hotel(hotel_id, name, stars, Address(address_id, street, city, zip_code))
            for hotel_id, name, stars, address_id, street, city, zip_code in hotels]

    def read_hotels_by_stars(self, min_stars: int) -> list[Hotel]:
        if min_stars is None:
            raise ValueError("Minimum stars is required")

        sql = """
        SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        LEFT JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Hotel.stars >= ?
        ORDER BY Hotel.stars DESC, Hotel.name
        """
        params = tuple([min_stars])
        hotels = self.fetchall(sql, params)
        
        return [Hotel(hotel_id, name, stars, 
                Address(address_id, street, city, zip_code) if address_id else None)
            for hotel_id, name, stars, address_id, street, city, zip_code in hotels]

    def read_hotels_by_city_and_stars(self, city: str, min_stars: int) -> list[Hotel]:
        if city is None:
            raise ValueError("City cannot be None")
        if min_stars is None:
            raise ValueError("Minimum stars is required")

        sql = """
        SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Address.city = ? AND Hotel.stars >= ?
        ORDER BY Hotel.stars DESC, Hotel.name
        """
        params = tuple([city, min_stars])
        hotels = self.fetchall(sql, params)
        
        return [Hotel(hotel_id, name, stars, 
                Address(address_id, street, city, zip_code))
            for hotel_id, name, stars, address_id, street, city, zip_code in hotels]

    def read_hotels_by_guest_capacity(self, city: str, max_guests: int) -> list[Hotel]:
        if city is None:
            raise ValueError("City cannot be None")
        if max_guests is None:
            raise ValueError("Maximum guests is required")

        sql = """
        SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        JOIN Room ON Hotel.hotel_id = Room.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Address.city = ? AND Room_Type.max_guests >= ?
        ORDER BY Hotel.stars DESC, Hotel.name
        """
        params = tuple([city, max_guests])
        hotels = self.fetchall(sql, params)
        
        return [Hotel(hotel_id, name, stars, 
                model.Address(address_id, street, city, zip_code))
            for hotel_id, name, stars, address_id, street, city, zip_code in hotels]

    def read_available_hotels(self, city: str, check_in_date: str, check_out_date: str) -> list[Hotel]:
        if city is None:
            raise ValueError("City cannot be None")
        if check_in_date is None:
            raise ValueError("Check-in date is required")
        if check_out_date is None:
            raise ValueError("Check-out date is required")

        sql = """
        SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        JOIN Room ON Hotel.hotel_id = Room.hotel_id
        WHERE Address.city = ? AND Room.room_id NOT IN (
            SELECT Booking.room_id FROM Booking
            WHERE Booking.is_cancelled = 0 AND (
                (Booking.check_in_date <= ? AND Booking.check_out_date > ?) OR
                (Booking.check_in_date < ? AND Booking.check_out_date >= ?)
            )
        )
        ORDER BY Hotel.stars DESC, Hotel.name
        """
        params = tuple([city, check_in_date, check_in_date, check_out_date, check_out_date])
        hotels = self.fetchall(sql, params)
        
        return [Hotel(hotel_id, name, stars, 
                model.Address(address_id, street, city, zip_code))
            for hotel_id, name, stars, address_id, street, city, zip_code in hotels]

    def read_all_hotels(self) -> list[Hotel]:
        sql = """
        SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        LEFT JOIN Address a ON Hotel.address_id = Address.address_id
        ORDER BY Hotel.name
        """
        hotels = self.fetchall(sql)
        
        return [Hotel(hotel_id, name,stars, 
                model.Address(address_id, street, city, zip_code) if address_id else None)
            for hotel_id, name, stars, address_id, street, city, zip_code in hotels]

    def update_hotel(self, hotel: Hotel) -> None:
        if hotel is None:
            raise ValueError("Hotel cannot be None")

        sql = """
        UPDATE Hotel SET name = ?, stars = ?, address_id = ? WHERE hotel_id = ?
        """
        params = tuple([hotel.name, hotel.stars, hotel.address.address_id if hotel.address else None, hotel.hotel_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_hotel(self, hotel: Hotel) -> None:
        if hotel is None:
            raise ValueError("Hotel cannot be None")

        sql = """
        DELETE FROM Hotel WHERE hotel_id = ?
        """
        params = tuple([hotel.hotel_id])
        last_row_id, row_count = self.execute(sql, params)