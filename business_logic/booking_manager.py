from datetime import datetime
import model
from model.booking import Booking
from data_access.booking_data_access import BookingDataAccess
from data_access.invoice_data_access import InvoiceDataAccess
from data_access.room_data_access import RoomDataAccess

class BookingManager:
    def __init__(self) -> None:
        self.__booking_dal = BookingDataAccess()
        self.__invoice_dal = InvoiceDataAccess()
        self.__room_dal = RoomDataAccess()

    # User Story 4.1: Buchung erstellen
    def create_booking(self, guest_id: int, room_id: int, check_in_date: datetime, 
                      check_out_date: datetime, total_amount: float = None) -> Booking:
        # Verfügbarkeit prüfen
        if not self.is_room_available(room_id, check_in_date, check_out_date):
            raise ValueError("Room is not available for the selected dates")
        
        # Preis berechnen wenn nicht angegeben
        if total_amount is None:
            total_amount = self.calculate_total_price(room_id, check_in_date, check_out_date)
        
        return self.__booking_dal.create_new_booking(guest_id, room_id, check_in_date, 
                                                   check_out_date, total_amount)

    # User Story 7: Dynamische Preisgestaltung
    def create_booking_with_dynamic_price(self, guest_id: int, room_id: int, 
                                        check_in_date: datetime, check_out_date: datetime) -> Booking:
        dynamic_price = self.calculate_dynamic_price(room_id, check_in_date, check_out_date)
        return self.create_booking(guest_id, room_id, check_in_date, check_out_date, dynamic_price)

    def calculate_dynamic_price(self, room_id: int, check_in_date: datetime, check_out_date: datetime) -> float:
        """User Story 7: Dynamische Preisgestaltung basierend auf Saison"""
        room = self.__room_dal.read_room_by_id(room_id)
        if room is None:
            raise ValueError("Room not found")
        
        base_price = room.price_per_night
        nights = (check_out_date - check_in_date).days
        month = check_in_date.month

        # Saisonale Faktoren
        if month in [7, 8]:  # Hochsaison: Juli, August
            factor = 1.2
        elif month in [1, 2]:  # Nebensaison: Januar, Februar
            factor = 0.85
        else:
            factor = 1.0

        total_price = base_price * nights * factor
        return round(total_price, 2)

    def calculate_total_price(self, room_id: int, check_in_date: datetime, check_out_date: datetime) -> float:
        """User Story 2.1: Gesamtpreis berechnen"""
        room = self.__room_dal.read_room_by_id(room_id)
        if room is None:
            raise ValueError("Room not found")
        
        nights = (check_out_date - check_in_date).days
        return room.price_per_night * nights

    # User Story 1.4: Verfügbarkeit prüfen
    def is_room_available(self, room_id: int, check_in_date: datetime, check_out_date: datetime) -> bool:
        conflicts = self.__booking_dal.read_conflicting_bookings(room_id, check_in_date, check_out_date)
        return len(conflicts) == 0

    # Read-Methoden
    def read_booking_by_id(self, booking_id: int) -> Booking | None:
        return self.__booking_dal.read_booking_by_id(booking_id)

    # User Story 12: Buchungshistorie
    def read_guest_bookings(self, guest_id: int) -> list[Booking]:
        return self.__booking_dal.read_bookings_by_guest_id(guest_id)

    # User Story 8: Alle Buchungen für Admin
    def read_all_bookings(self) -> list[Booking]:
        return self.__booking_dal.read_all_bookings()

    # User Story 6: Buchung stornieren
    def cancel_booking(self, booking_id: int) -> str:
        # Buchung stornieren
        success = self.__booking_dal.update_booking_status(booking_id, True)
        if not success:
            return f"Failed to cancel booking {booking_id}"
        
        # Rechnung löschen falls vorhanden
        try:
            invoice = self.__invoice_dal.read_invoice_by_booking_id(booking_id)
            if invoice:
                self.__invoice_dal.delete_invoice(invoice.invoice_id)
                return f"Booking {booking_id} cancelled. Invoice {invoice.invoice_id} deleted."
            else:
                return f"Booking {booking_id} cancelled. No invoice found."
        except:
            return f"Booking {booking_id} cancelled. Error handling invoice."

    # User Story 11: Buchung bearbeiten
    def update_booking(self, booking_id: int, check_in_date: datetime = None, 
                      check_out_date: datetime = None) -> bool:
        # Bei Datumsänderung Verfügbarkeit prüfen
        if check_in_date or check_out_date:
            booking = self.read_booking_by_id(booking_id)
            if booking:
                new_check_in = check_in_date or booking.check_in_date
                new_check_out = check_out_date or booking.check_out_date
                
                if not self.is_room_available(booking.room.room_id, new_check_in, new_check_out):
                    raise ValueError("Room is not available for the new dates")
                
                # Neuen Gesamtpreis berechnen
                new_total = self.calculate_total_price(booking.room.room_id, new_check_in, new_check_out)
                return self.__booking_dal.update_booking(booking_id, new_check_in, new_check_out, new_total)
        
        return self.__booking_dal.update_booking(booking_id, check_in_date, check_out_date)

    def delete_booking(self, booking_id: int) -> bool:
        return self.__booking_dal.delete_booking(booking_id)