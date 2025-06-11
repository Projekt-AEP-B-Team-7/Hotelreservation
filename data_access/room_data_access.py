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

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_room(self, hotel: Hotel, room_number: str, room_type: RoomType, price_per_night: float) -> Room:
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
        return Room(last_row_id, hotel, room_number, room_type, price_per_night)

    def read_room_by_id(self, room_id: int) -> Room | None:
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
                address = Address(address_id, street, city, zip_code)
            
            hotel = Hotel(hotel_id, hotel_name, hotel_stars, address)
            room_type = RoomType(type_id, type_description, max_guests)
            
            return Room(room_id, hotel, room_number, room_type, price_per_night)
        else:
            return None

    def read_rooms_by_hotel(self, hotel: Hotel) -> list[Room]:
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
        
        return [Room(room_id, hotel, room_number, RoomType(type_id, description, max_guests), price_per_night)
            for room_id, room_number, price_per_night, type_id, description, max_guests in rooms]

    def read_all_rooms_with_facilities(self) -> list[Room]:
        sql = """
        SELECT Room.room_id, Room.room_number, Room.price_per_night,
        Room_Type.type_id, Room_Type.description, Room_Type.max_guests,
        Hotel.hotel_id, Hotel.name, Hotel.stars,
        Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Room
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
        LEFT JOIN Address ON Hotel.address_id = Address.address_id
        ORDER BY Room.room_number
        """
        rooms = self.fetchall(sql)

        result = []
        
        for (room_id, room_number, price_per_night, type_id, type_description, max_guests,
            hotel_id, hotel_name, hotel_stars, address_id, street, city, zip_code) in rooms:
            
            address = Address(address_id, street, city, zip_code) if address_id else None
            hotel = Hotel(hotel_id, hotel_name, hotel_stars, address)
            room_type = RoomType(type_id, type_description, max_guests)
            room = Room(room_id, hotel, room_number, room_type, price_per_night)
            result.append(room)
        return result

    def read_available_rooms_by_hotel(self, hotel: Hotel, check_in_date: str, check_out_date: str) -> list[Room]:
        sql = """
        SELECT Room.room_id, Room.hotel_id, Room.room_number, Room.price_per_night,
            Room_Type.type_id, Room_Type.description, Room_Type.max_guests
        FROM Room
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Room.hotel_id = ?
        AND Room.room_id NOT IN (
            SELECT Booking.room_id
            FROM Booking
            WHERE Booking.is_cancelled = 0 AND (
                (Booking.check_in_date <= ? AND Booking.check_out_date > ?) OR
                (Booking.check_in_date < ? AND Booking.check_out_date >= ?)
            )
        )
        ORDER BY Room.room_number
        """
        rows = self.fetchall(sql, (hotel.hotel_id, check_in_date, check_in_date, check_out_date, check_out_date))
        
        available_rooms = []
        for row in rows:
            room_id, hotel_id, room_number, price_per_night, type_id, description, max_guests = row
            room_type = RoomType(type_id, description, max_guests)
            room = Room(room_id, hotel, room_number, room_type, price_per_night)
            available_rooms.append(room)
        
        return available_rooms

    def read_rooms_by_hotel_id(self, hotel_id: int) -> list[Room]:
        if hotel_id is None:
            raise ValueError("Hotel ID is required")

        sql = """
        SELECT Room.room_id, Room.room_number, Room.price_per_night,
            Room_Type.type_id, Room_Type.description, Room_Type.max_guests,
            Hotel.hotel_id, Hotel.name, Hotel.stars
        FROM Room
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
        WHERE Hotel.hotel_id = ?
        ORDER BY Room.room_number
        """
        params = (hotel_id,)
        results = self.fetchall(sql, params)

        return [
            Room(
                room_id,
                Hotel(hotel_id, hotel_name, hotel_stars),
                room_number,
                RoomType(type_id, description, max_guests),
                price_per_night
            )
            for room_id, room_number, price_per_night,
                type_id, description, max_guests,
                hotel_id, hotel_name, hotel_stars in results
        ]

    def update_room(self, room: Room) -> None:
        if room is None:
            raise ValueError("Room cannot be None")

        sql = """
        UPDATE Room SET hotel_id = ?, room_number = ?, type_id = ?, price_per_night = ? WHERE room_id = ?
        """
        params = tuple([room.hotel.hotel_id, room.room_number, room.room_type.type_id, room.price_per_night, room.room_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_room(self, room: Room) -> None:
        if room is None:
            raise ValueError("Room cannot be None")

        sql = """
        DELETE FROM Room WHERE room_id = ?
        """
        params = tuple([room.room_id])
        last_row_id, row_count = self.execute(sql, params)