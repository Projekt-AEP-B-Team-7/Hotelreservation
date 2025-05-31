from __future__ import annotations
from datetime import date
import model
from data_access.base_data_access import BaseDataAccess

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_invoice(self, booking: model.Booking, issue_date: date, total_amount: float) -> model.Invoice:
        if booking is None:
            raise ValueError("Booking is required")
        if issue_date is None:
            raise ValueError("Issue date is required")
        if total_amount is None:
            raise ValueError("Total amount is required")

        sql = """
        INSERT INTO Invoice (booking_id, issue_date, total_amount) VALUES (?, ?, ?)
        """
        params = (booking.booking_id, issue_date, total_amount)
        last_row_id, row_count = self.execute(sql, params)
        return model.Invoice(last_row_id, booking, issue_date, total_amount)

    def read_invoice_by_id(self, invoice_id: int) -> model.Invoice | None:
        if invoice_id is None:
            raise ValueError("Invoice ID is required")

        sql = """
        SELECT Invoice.invoice_id, Invoice.booking_id, Invoice.issue_date, Invoice.total_amount,
               Booking.guest_id, Booking.room_id, Booking.check_in_date, Booking.check_out_date, 
               Booking.is_cancelled, Booking.total_amount AS "Booking amount",
               Guest.first_name, Guest.last_name, Guest.email,
               Room.room_number, Room.price_per_night,
               Hotel.hotel_id, Hotel.name AS "Hotel Name", Hotel.stars,
               Room_Type.type_id, Room_Type.description, Room_Type.max_guests
        FROM Invoice
        JOIN Booking ON Invoice.booking_id = Booking.booking_id
        JOIN Guest ON Booking.guest_id = Guest.guest_id
        JOIN Room ON Booking.room_id = Room.room_id
        JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Invoice.invoice_id = ?
        """
        params = tuple([invoice_id])
        result = self.fetchone(sql, params)
        if result:
            (invoice_id, booking_id, issue_date, total_amount,
             guest_id, room_id, check_in_date, check_out_date, is_cancelled, booking_amount,
             first_name, last_name, email, room_number, price_per_night,
             hotel_id, hotel_name, hotel_stars, type_id, type_description, max_guests) = result
            
            guest = model.Guest(guest_id, first_name, last_name, email)
            hotel = model.Hotel(hotel_id, hotel_name, hotel_stars)
            room_type = model.RoomType(type_id, type_description, max_guests)
            room = model.Room(room_id, hotel, room_number, room_type, price_per_night)
            booking = model.Booking(booking_id, guest, room, check_in_date, check_out_date, is_cancelled, booking_amount)
            
            return model.Invoice(invoice_id, booking, issue_date, total_amount)
        else:
            return None