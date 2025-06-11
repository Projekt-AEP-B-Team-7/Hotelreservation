from __future__ import annotations
from datetime import date
from model.room_type import RoomType
from model.hotel import Hotel
from model.booking import Booking
from model.facilities import Facilities
from model.address import Address
from model.guest import Guest
from model.room import Room
from model.invoice import Invoice
from data_access.base_data_access import BaseDataAccess

class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_booking(self, guest: Guest, room: Room, check_in_date: date, 
                          check_out_date: date, total_amount: float) -> Booking:
        if guest is None:
            raise ValueError("Guest is required")
        if room is None:
            raise ValueError("Room is required")
        if check_in_date is None:
            raise ValueError("Check-in date is required")
        if check_out_date is None:
            raise ValueError("Check-out date is required")
        if total_amount is None:
            raise ValueError("Total amount is required")

        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount) 
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (guest.guest_id, room.room_id, check_in_date, check_out_date, False, total_amount)
        last_row_id, row_count = self.execute(sql, params)
        return Booking(last_row_id, guest, room, check_in_date, check_out_date, False, total_amount)

    def read_booking_by_id(self, booking_id: int) -> Booking | None:
        if booking_id is None:
            raise ValueError("Booking ID is required")

        sql = """
        SELECT Booking.booking_id, Booking.guest_id, Booking.room_id, Booking.check_in_date, Booking.check_out_date, 
               Booking.is_cancelled, Booking.total_amount,
               Guest.first_name AS "First Name", Guest.last_name AS "Last Name", Guest.email, Guest.phone_number,
               Room.room_number, Room.price_per_night,
               Hotel.hotel_id, Hotel.name AS "Hotel Name", Hotel.stars,
               Room_Type.type_id, Room_Type.description, Room_Type.max_guests,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Booking
        JOIN Guest ON Booking.guest_id = Guest.guest_id
        JOIN Room ON Booking.room_id = Room.room_id
        JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        LEFT JOIN Address ON Guest.address_id = Address.address_id
        WHERE Booking.booking_id = ?
        """
        params = tuple([booking_id])
        result = self.fetchone(sql, params)
        if result:
            (booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount,
             first_name, last_name, email, phone_number, room_number, price_per_night,
             hotel_id, hotel_name, hotel_stars, type_id, type_description, max_guests,
             address_id, street, city, zip_code) = result
            
            guest_address = None
            if address_id:
                guest_address = Address(address_id, street, city, zip_code)
            
            guest = Guest(guest_id, first_name, last_name, email, phone_number, guest_address)
            hotel = Hotel(hotel_id, hotel_name, hotel_stars)
            room_type = RoomType(type_id, type_description, max_guests)
            room = Room(room_id, hotel, room_number, room_type, price_per_night)
            
            return Booking(booking_id, guest, room, check_in_date, check_out_date, bool(is_cancelled), total_amount)
        else:
            return None

    def read_bookings_by_guest(self, guest: Guest) -> list[Booking]:
        if guest is None:
            raise ValueError("Guest cannot be None")

        sql = """
        SELECT Booking.booking_id, Booking.room_id, Booking.check_in_date, Booking.check_out_date, 
               Booking.is_cancelled, Booking.total_amount,
               Room.room_number, Room.price_per_night,
               Hotel.hotel_id, Hotel.name as "Hotel Name", Hotel.stars,
               Room_Type.type_id, Room_Type.description, Room_Type.max_guests
        FROM Booking
        JOIN Room ON Booking.room_id = Room.room_id
        JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Booking.guest_id = ?
        ORDER BY Booking.check_in_date DESC
        """
        params = tuple([guest.guest_id])
        bookings = self.fetchall(sql, params)
        
        return [Booking(booking_id, guest, Room(room_id, Hotel(hotel_id, hotel_name, hotel_stars),
                room_number, RoomType(type_id, description, max_guests), price_per_night),
                check_in_date, check_out_date, bool(is_cancelled), total_amount)
            for booking_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount,
                room_number, price_per_night, hotel_id, hotel_name, hotel_stars,
                type_id, description, max_guests in bookings]

    def read_bookings_by_room(self, room: Room) -> list[Booking]:
        if room is None:
            raise ValueError("Room cannot be None")

        sql = """
        SELECT Booking.booking_id, Booking.guest_id, Booking.check_in_date, Booking.check_out_date, 
               Booking.is_cancelled, Booking.total_amount,
               Guest.first_name, Guest.last_name, Guest.email, Guest.phone_number
        FROM Booking
        JOIN Guest ON Booking.guest_id = Guest.guest_id
        WHERE Booking.room_id = ?
        ORDER BY Booking.check_in_date DESC
        """
        params = tuple([room.room_id])
        bookings = self.fetchall(sql, params)
        
        return [Booking(booking_id, Guest(guest_id, first_name, last_name, email, phone_number, None),
                room, check_in_date, check_out_date, bool(is_cancelled), total_amount)
            for booking_id, guest_id, check_in_date, check_out_date, is_cancelled, total_amount,
                first_name, last_name, email, phone_number in bookings]

    def read_bookings_by_hotel(self, hotel: Hotel) -> list[Booking]:
        if hotel is None:
            raise ValueError("Hotel cannot be None")

        sql = """
        SELECT Booking.booking_id, Booking.guest_id, Booking.room_id, Booking.check_in_date, Booking.check_out_date, 
               Booking.is_cancelled, Booking.total_amount,
               Guest.first_name, Guest.last_name, Guest.email, Guest.phone_number,
               Room.room_number, Room.price_per_night,
               Room_Type.type_id, Room_Type.description, Room_Type.max_guests
        FROM Booking
        JOIN Guest ON Booking.guest_id = Guest.guest_id
        JOIN Room ON Booking.room_id = Room.room_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Room.hotel_id = ?
        ORDER BY Booking.check_in_date DESC
        """
        params = tuple([hotel.hotel_id])
        bookings = self.fetchall(sql, params)
        
        return [Booking(booking_id, Guest(guest_id, first_name, last_name, email, phone_number, None),
                Room(room_id, hotel, room_number, RoomType(type_id, description, max_guests), price_per_night),
                check_in_date, check_out_date, bool(is_cancelled), total_amount)
            for booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount,
                first_name, last_name, email, phone_number, room_number, price_per_night,
                type_id, description, max_guests in bookings]

    def read_all_bookings(self) -> list[Booking]:
        sql = """
        SELECT Booking.booking_id, Booking.guest_id, Booking.room_id, Booking.check_in_date, Booking.check_out_date, 
               Booking.is_cancelled, Booking.total_amount,
               Guest.first_name, Guest.last_name, Guest.email, Guest.phone_number,
               Room.room_number, Room.price_per_night,
               Hotel.hotel_id, Hotel.name AS "Hotel Name", Hotel.stars,
               Room_Type.type_id, Room_Type.description, Room_Type.max_guests
        FROM Booking
        JOIN Guest ON Booking.guest_id = Guest.guest_id
        JOIN Room ON Booking.room_id = Room.room_id
        JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        ORDER BY Booking.booking_id DESC
        """
        bookings = self.fetchall(sql)
        
        return [Booking(booking_id, Guest(guest_id, first_name, last_name, email, phone_number, None),
                Room(room_id, Hotel(hotel_id, hotel_name, hotel_stars),
                    room_number, RoomType(type_id, description, max_guests), price_per_night),
                check_in_date, check_out_date, bool(is_cancelled), total_amount)
            for booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount,
                first_name, last_name, email, phone_number, room_number, price_per_night,
                hotel_id, hotel_name, hotel_stars, type_id, description, max_guests in bookings]

    def read_active_bookings(self) -> list[Booking]:
        sql = """
        SELECT Booking.booking_id, Booking.guest_id, Booking.room_id, Booking.check_in_date, Booking.check_out_date, 
               Booking.is_cancelled, Booking.total_amount,
               Guest.first_name, Guest.last_name, Guest.email, Guest.phone_number,
               Room.room_number, Room.price_per_night,
               Hotel.hotel_id, Hotel.name AS "Hotel Name", Hotel.stars,
               Room_Type.type_id, Room_Type.description, Room_Type.max_guests
        FROM Booking
        JOIN Guest ON Booking.guest_id = Guest.guest_id
        JOIN Room ON Booking.room_id = Room.room_id
        JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Booking.is_cancelled = 0
        ORDER BY Booking.check_in_date DESC
        """
        bookings = self.fetchall(sql)
        
        return [Booking(booking_id, Guest(guest_id, first_name, last_name, email, phone_number, None),
                Room(room_id, Hotel(hotel_id, hotel_name, hotel_stars),
                    room_number, RoomType(type_id, description, max_guests), price_per_night),
                check_in_date, check_out_date, bool(is_cancelled), total_amount)
            for booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount,
                first_name, last_name, email, phone_number, room_number, price_per_night,
                hotel_id, hotel_name, hotel_stars, type_id, description, max_guests in bookings]

    def read_cancelled_bookings(self) -> list[Booking]:
        sql = """
        SELECT Booking.booking_id, Booking.guest_id, Booking.room_id, Booking.check_in_date, Booking.check_out_date, 
               Booking.is_cancelled, Booking.total_amount,
               Guest.first_name, Guest.last_name, Guest.email, Guest.phone_number,
               Room.room_number, Room.price_per_night,
               Hotel.hotel_id, Hotel.name AS "Hotel Name", Hotel.stars,
               Room_Type.type_id, Room_Type.description, Room_Type.max_guests
        FROM Booking
        JOIN Guest ON Booking.guest_id = Guest.guest_id
        JOIN Room ON Booking.room_id = Room.room_id
        JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Booking.is_cancelled = 1
        ORDER BY Booking.check_in_date DESC
        """
        bookings = self.fetchall(sql)
        
        return [Booking(booking_id, Guest(guest_id, first_name, last_name, email, phone_number, None),
                Room(room_id, Hotel(hotel_id, hotel_name, hotel_stars), room_number,
                    RoomType(type_id, description, max_guests), price_per_night),
                check_in_date, check_out_date, bool(is_cancelled), total_amount)
            for booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount,
                first_name, last_name, email, phone_number, room_number, price_per_night,
                hotel_id, hotel_name, hotel_stars, type_id, description, max_guests in bookings]

    def update_booking(self, booking: Booking) -> None:
        if booking is None:
            raise ValueError("Booking cannot be None")

        sql = """
        UPDATE Booking SET guest_id = ?, room_id = ?, check_in_date = ?, check_out_date = ?, 
                          is_cancelled = ?, total_amount = ? 
        WHERE booking_id = ?
        """
        params = tuple([booking.guest.guest_id, booking.room.room_id, booking.check_in_date, booking.check_out_date,
            booking.is_cancelled, booking.total_amount, booking.booking_id])
        last_row_id, row_count = self.execute(sql, params)

    def cancel_booking(self, booking: Booking) -> None:
        if booking is None:
            raise ValueError("Booking cannot be None")
        
        sql = """
        UPDATE Booking SET is_cancelled = 1 WHERE booking_id = ?
        """
        params = tuple([booking.booking_id])
        last_row_id, row_count = self.execute(sql, params)

    def cancel_booking_by_id(self, booking_id: int) -> bool:
        sql = """
        UPDATE Booking SET is_cancelled = 1 WHERE booking_id = ? AND is_cancelled = 0
        """
        params = tuple([booking_id])
        last_row_id, row_count = self.execute(sql, params)
        return row_count > 0
       
    def delete_booking(self, booking: Booking) -> None:
        if booking is None:
            raise ValueError("Booking cannot be None")

        sql = """
        DELETE FROM Booking WHERE booking_id = ?
        """
        params = tuple([booking.booking_id])
        last_row_id, row_count = self.execute(sql, params)