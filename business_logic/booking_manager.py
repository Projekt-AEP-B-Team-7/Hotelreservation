from datetime import date, datetime
from model.booking import Booking
from data_access.booking_data_access import BookingDataAccess
from model.invoice import Invoice
from model.room import Room
from model.guest import Guest
from model.hotel import Hotel


class BookingManager:
    def __init__(self):
        self.__booking_da = BookingDataAccess()

    def create_booking(self, guest: Guest, room: Room, check_in_date: date, 
                      check_out_date: date, total_amount: float) -> Booking:
        return self.__booking_da.create_new_booking(guest, room, check_in_date, check_out_date, total_amount)

    def read_booking(self, booking_id: int) -> Booking:
        return self.__booking_da.read_booking_by_id(booking_id)

    def read_bookings_by_guest(self, guest: Guest) -> list[Booking]:
        return self.__booking_da.read_bookings_by_guest(guest)

    def read_bookings_by_room(self, room: Room) -> list[Booking]:
        return self.__booking_da.read_bookings_by_room(room)

    def read_bookings_by_hotel(self, hotel: Hotel) -> list[Booking]:
        return self.__booking_da.read_bookings_by_hotel(hotel)

    def read_all_bookings(self) -> list[Booking]:
        return self.__booking_da.read_all_bookings()

    def read_active_bookings(self) -> list[Booking]:
        return self.__booking_da.read_active_bookings()

    def read_cancelled_bookings(self) -> list[Booking]:
        return self.__booking_da.read_cancelled_bookings()

    def update_booking(self, booking: Booking) -> None:
        self.__booking_da.update_booking(booking)

    def cancel_booking(self, booking: Booking) -> None:
        booking.is_cancelled = True
        self.__booking_da.cancel_booking(booking)
    
    def cancel_booking_by_id(self, booking_id: int) -> None:
        return self.__booking_da.cancel_booking_by_id(booking_id)

    def delete_booking(self, booking: Booking) -> None:
        self.__booking_da.delete_booking(booking)