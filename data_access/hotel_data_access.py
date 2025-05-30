from __future__ import annotations

from model.hotel import Hotel
from model.address import Address
from model.room import Room
from model.room_type import RoomType

from data_access.base_data_access import BaseDataAccess

class HotelDataAccess(BaseDataAccess):
    
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_hotel_by_name(self, name: str) -> model.Hotel | None:
        sql = """
        SELECT Hotel_id, Name, Stars FROM Hotel WHERE Name = ?;
        """
        params = tuple([name])
        result = self.fetchone(sql, params)
        if result:
            hotel_id, name, stars = result
            return model.Hotel(hotel_id, name, stars)
        else:
            return None

    def read_hotel_by_city(self, city: str) -> list[Hotel]:
        sql = """
        SELECT Hotel.Hotel_id, Hotel.Name, Hotel.Stars, Address.Street, Address.Zip_Code, Address.City
        FROM Hotel
        JOIN Address ON Hotel.Address_Id = Address.Address_Id
        WHERE Address.City = ?;
        """
        params = tuple([city])
        result = self.fetchall(sql, params)

        hotels = []
        for row in result:
            hotel_id, name, stars, street, zip_code, city = row
            address = Address(None, street, zip_code, city)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels
    
    def read_hotels_by_city_and_stars(self, city: str, stars: int) -> list[Hotel]:
        sql = """
        SELECT Hotel.Hotel_id, Hotel.Name, Hotel.Stars, Address.Street, Address.Zip_Code, Address.City
        FROM Hotel
        JOIN Address ON Hotel.Address_Id = Address.Address_Id
        WHERE Address.City = ? AND Hotel.Stars >= ?;
        """
        params = (city, stars)
        result = self.fetchall(sql, params)

        hotels = []
        for row in result:
            hotel_id, name, stars, street, zip_code, city = row
            address = Address(None, street, zip_code, city)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels

    def read_available_hotels_combined(self, city: str, max_guests: int) -> list[Hotel]:
        sql = """
        SELECT DISTINCT
        Hotel.Hotel_id, Hotel.name, Address.street, Address.city, Address.zip_code, Hotel.stars, Room_Type.description, Room_Type.max_guests, Room.price_per_night
        FROM Hotel 
        JOIN Room On Hotel.hotel_id = Room.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Address.city = ? AND Room_Type.max_guests >= ?;
        """
        params = tuple([city, max_guests])
        result = self.fetchall(sql, params)
        
        hotels = []
        for row in result:
            hotel_id, name, street, city, zip_code, stars, description, max_guests, price = row
            address = Address(None, street, city, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels

    def get_available_hotels(self, city: str, check_in: str, check_out:str, max_guests: int) -> list[Hotel]:
        sql = """
        SELECT DISTINCT
        Hotel.Hotel_id, Hotel.name, Address.street, Address.city, Address.zip_code, Hotel.stars, Room_Type.description, Room_Type.max_guests, Room.price_per_night
        FROM Hotel 
        JOIN Room On Hotel.hotel_id = Room.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Address.city = ? AND Room_Type.max_guests >= ?;
        """
        params = tuple([city, max_guests])
        result = self.fetchall(sql, params)
        
        hotels = []
        for row in result:
            hotel_id, name, street, city, zip_code, stars, description, max_guests, price = row
            address = Address(None, street, city, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels




    def update_hotel_name(self, name: str) -> model.Hotel:
        if hotel is None:
            raise ValueError("Hotel Name cannot be None")

        sql = """
        UPDATE Hotel SET Name = ? WHERE hotel_id = ?
        """
        params = tuple([name, hotel_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_hotel(self, hotel_id) -> model.Hotel:
        if hotel is None:
            raise ValueError("Hotel cannot be None")

        sql = """
        DELETE FROM Hotel WHERE hotel_id = ?
        """
        params = tuple([hotel_id])
        last_row_id, row_count = self.execute(sql, params)
    