from __future__ import annotations
import model
from data_access.base_data_access import BaseDataAccess

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_room(self, hotel: model.Hotel, room_number: str, room_type: model.RoomType, price_per_night: float) -> model.Room:
        if hotel is None:
            raise ValueError("Hotel is required")
        if room_number is None:
            raise ValueError("Room number is required")
        if room_type is None:
            raise ValueError("Room type is required")
        if price_per_night is None:
            raise ValueError("Price per night is required")

        sql = """
        INSERT INTO Room (hotel_id, room_number, type_id, price_per_night) VALUES (?, ?, ?, ?)
        """
        params = (hotel.hotel_id, room_number, room_type.type_id, price_per_night)
        last_row_id, row_count = self.execute(sql, params)
        return model.Room(last_row_id, hotel, room_number, room_type, price_per_night)

    def read_room_by_id(self, room_id: int) -> model.Room | None:
        if room_id is None:
            raise ValueError("Room ID is required")

        sql = """
        SELECT Room.room_id, Room.hotel_id, Room.room_number, Room.type_id, Room.price_per_night,
               Hotel.name AS "Hotel Name", Hotel.stars, Room_Type.description, Room_Type.max_guests,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Room
        JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        LEFT JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Room.room_id = ?
        """
        params = tuple([room_id])
        result = self.fetchone(sql, params)
        if result:
            (room_id, hotel_id, room_number, type_id, price_per_night,
             hotel_name, hotel_stars, type_description, max_guests,
             address_id, street, city, zip_code) = result
            
            address = None
            if address_id:
                address = model.Address(address_id, street, city, zip_code)
            
            hotel = model.Hotel(hotel_id, hotel_name, hotel_stars, address)
            room_type = model.RoomType(type_id, type_description, max_guests)
            
            return model.Room(room_id, hotel, room_number, room_type, price_per_night)
        else:
            return None

    def read_rooms_by_hotel(self, hotel: model.Hotel) -> list[model.Room]:
        if hotel is None:
            raise ValueError("Hotel cannot be None")

        sql = """
        SELECT Room.room_id, Room.room_number, Room.price_per_night,
               Room_Type.type_id, Room_Type.description, Room_Type.max_guests
        FROM Room
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Room.hotel_id = ?
        ORDER BY Room.room_number
        """
        params = tuple([hotel.hotel_id])
        rooms = self.fetchall(sql, params)
        
        return [model.Room(room_id, hotel, room_number, model.RoomType(type_id, description, max_guests), price_per_night)
            for room_id, room_number, price_per_night, type_id, description, max_guests in rooms]