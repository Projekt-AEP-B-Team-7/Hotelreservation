from datetime import datetime
import model
import data_access

class BookingManager:
    def __init__(self) -> None:
        self.__booking_dal = data_access.BookingDataAccess()
        self.__invoice_dal = data_access.InvoiceDataAccess()

    def create_booking(self, guest_id: int, room_id: int, check_in_date: str, check_out_date: str, is_cancelled: bool, total_amount: float) -> model.Booking:
        return self.__booking_dal.create_new_booking(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)

    def create_booking_with_dynamic_price(self, guest_id: int, room_id: int, check_in_date: str, check_out_date: str) -> model.Booking:
        dynamic_price = self.calculate_dynamic_price(room_id, check_in_date)
        return self.create_booking(guest_id, room_id, check_in_date, check_out_date, is_cancelled=False, total_amount=dynamic_price)

    def calculate_dynamic_price(self, room_id: int, check_in_date: str) -> float:
        room = self.__booking_dal.get_room_by_id(room_id)
        if room is None:
            raise ValueError("Zimmer wurde nicht gefunden.")
        
        base_price = room.price_per_night
        month = datetime.strptime(check_in_date, "%Y-%m-%d").month

        if month in [7, 8]:  # Hochsaison: Juli, August
            factor = 1.2
        elif month in [1, 2]:  # Nebensaison: Januar, Februar
            factor = 0.85
        else:
            factor = 1.0

        return round(base_price * factor, 2)

    def read_booking_by_guest_id(self, guest_id: int) -> model.Booking | None:
        return self.__booking_dal.read_booking_by_guestId(guest_id)

    def cancel_booking(self, booking_id: int) -> str:
        self.__booking_dal.update_booking_status(booking_id, is_cancelled=True)
        invoice = self.__invoice_dal.read_invoice_by_bookingID(booking_id)
        if invoice:
            self.__invoice_dal.delete_invoice(invoice.invoice_id)
            return f"Buchung {booking_id} wurde storniert. Rechnung {invoice.invoice_id} gelöscht."
        else:
            return f"Buchung {booking_id} wurde storniert. Es war keine Rechnung vorhanden."

    def delete_booking(self, booking_id: int) -> None:
        self.__booking_dal.delete_booking(booking_id)

    def read_all_bookings(self) -> list[model.Booking]:
        return self.__booking_dal.read_all_bookings()
