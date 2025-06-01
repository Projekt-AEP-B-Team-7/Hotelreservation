from datetime import datetime
import model
from model.booking import Booking
from data_access.booking_data_access import BookingDataAccess
from data_access.invoice_data_access import InvoiceDataAccess
from data_access.room_data_access import RoomDataAccess

class BookingManager:
    def __init__(self):
        self.__booking_da = data_access.BookingDataAccess()

    def create_booking(self, guest: model.Guest, room: model.Room, check_in_date: date, 
                      check_out_date: date, total_amount: float) -> model.Booking:
        return self.__booking_da.create_new_booking(guest, room, check_in_date, check_out_date, total_amount)

    def read_booking(self, booking_id: int) -> model.Booking:
        return self.__booking_da.read_booking_by_id(booking_id)

    def read_bookings_by_guest(self, guest: model.Guest) -> list[model.Booking]:
        return self.__booking_da.read_bookings_by_guest(guest)

    def read_bookings_by_room(self, room: model.Room) -> list[model.Booking]:
        return self.__booking_da.read_bookings_by_room(room)

    def read_bookings_by_hotel(self, hotel: model.Hotel) -> list[model.Booking]:
        return self.__booking_da.read_bookings_by_hotel(hotel)

    def read_all_bookings(self) -> list[model.Booking]:
        return self.__booking_da.read_all_bookings()

    def read_active_bookings(self) -> list[model.Booking]:
        return self.__booking_da.read_active_bookings()

    def read_cancelled_bookings(self) -> list[model.Booking]:
        return self.__booking_da.read_cancelled_bookings()

    def update_booking(self, booking: model.Booking) -> None:
        self.__booking_da.update_booking(booking)

    def cancel_booking(self, booking: model.Booking) -> None:
        booking.is_cancelled = True
        self.__booking_da.cancel_booking(booking)

    def delete_booking(self, booking: model.Booking) -> None:
        self.__booking_da.delete_booking(booking)