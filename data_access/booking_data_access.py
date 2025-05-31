from __future__ import annotations
from datetime import datetime
import model
from model.booking import Booking
from model.room import Room
from model.guest import Guest
from data_access.base_data_access import BaseDataAccess

class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
    
    # User Story 4.1: Buchung erstellen
    def create_new_booking(self, guest_id: int, room_id: int, check_in_date: datetime, 
                          check_out_date: datetime, total_amount: float) -> Booking:
        if not guest_id:
            raise ValueError("Guest ID is required")
        if not room_id:
            raise ValueError("Room ID is required")
        if not check_in_date:
            raise ValueError("Check in date is required")
        if not check_out_date:
            raise ValueError("Check out date is required")
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")
    
        sql = """
        INSERT INTO Booking (Guest_id, Room_id, Check_in_date, Check_out_date, 
                           Total_amount, Is_cancelled, Booking_date) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (guest_id, room_id, check_in_date, check_out_date, 
                 total_amount, False, datetime.now())

        last_row_id, row_count = self.execute(sql, params)
        
        # Room-Objekt laden für vollständiges Booking
        room = self._load_room_by_id(room_id)
        return Booking(last_row_id, guest_id, room, check_in_date, 
                      check_out_date, False, total_amount)

    def read_booking_by_id(self, booking_id: int) -> Booking | None:
        sql = """
        SELECT b.Booking_id, b.Guest_id, b.Room_id, b.Check_in_date, 
               b.Check_out_date, b.Total_amount, b.Is_cancelled, b.Booking_date
        FROM Booking b 
        WHERE b.Booking_id = ?
        """
        params = tuple([booking_id])
        result = self.fetchone(sql, params)
        if result:
            booking_id, guest_id, room_id, check_in, check_out, total_amount, is_cancelled, booking_date = result
            room = self._load_room_by_id(room_id)
            return Booking(booking_id, guest_id, room, check_in, check_out, is_cancelled, total_amount)
        return None

    # User Story 12: Buchungen nach Gast
    def read_bookings_by_guest_id(self, guest_id: int) -> list[Booking]:
        sql = """
        SELECT b.Booking_id, b.Guest_id, b.Room_id, b.Check_in_date, 
               b.Check_out_date, b.Total_amount, b.Is_cancelled, b.Booking_date
        FROM Booking b 
        WHERE b.Guest_id = ?
        ORDER BY b.Check_in_date DESC
        """
        params = tuple([guest_id])
        result = self.fetchall(sql, params)
        
        bookings = []
        for row in result:
            booking_id, guest_id, room_id, check_in, check_out, total_amount, is_cancelled, booking_date = row
            room = self._load_room_by_id(room_id)
            booking = Booking(booking_id, guest_id, room, check_in, check_out, is_cancelled, total_amount)
            bookings.append(booking)
        return bookings

    # User Story 8: Alle Buchungen für Admin
    def read_all_bookings(self) -> list[Booking]:
        sql = """
        SELECT b.Booking_id, b.Guest_id, b.Room_id, b.Check_in_date, 
               b.Check_out_date, b.Total_amount, b.Is_cancelled, b.Booking_date,
               h.Name as hotel_name, g.First_name, g.Last_name
        FROM Booking b
        JOIN Room r ON b.Room_id = r.Room_id
        JOIN Hotel h ON r.Hotel_id = h.Hotel_id
        JOIN Guest g ON b.Guest_id = g.Guest_id
        ORDER BY b.Booking_date DESC
        """
        result = self.fetchall(sql, tuple())
        
        bookings = []
        for row in result:
            booking_id, guest_id, room_id, check_in, check_out, total_amount, is_cancelled, booking_date, hotel_name, first_name, last_name = row
            room = self._load_room_by_id(room_id)
            booking = Booking(booking_id, guest_id, room, check_in, check_out, is_cancelled, total_amount)
            bookings.append(booking)
        return bookings

    # User Story 1.4: Verfügbarkeit prüfen
    def read_conflicting_bookings(self, room_id: int, check_in: datetime, check_out: datetime) -> list[Booking]:
        sql = """
        SELECT b.Booking_id, b.Guest_id, b.Room_id, b.Check_in_date, 
               b.Check_out_date, b.Total_amount, b.Is_cancelled, b.Booking_date
        FROM Booking b 
        WHERE b.Room_id = ? AND b.Is_cancelled = 0 AND (
            (b.Check_in_date <= ? AND b.Check_out_date > ?) OR
            (b.Check_in_date < ? AND b.Check_out_date >= ?)
        )
        """
        params = (room_id, check_in, check_in, check_out, check_out)
        result = self.fetchall(sql, params)
        
        bookings = []
        for row in result:
            booking_id, guest_id, room_id, check_in_db, check_out_db, total_amount, is_cancelled, booking_date = row
            room = self._load_room_by_id(room_id)
            booking = Booking(booking_id, guest_id, room, check_in_db, check_out_db, is_cancelled, total_amount)
            bookings.append(booking)
        return bookings

    # User Story 6: Buchung stornieren
    def update_booking_status(self, booking_id: int, is_cancelled: bool) -> bool:
        sql = """
        UPDATE Booking SET Is_cancelled = ? WHERE Booking_id = ?
        """
        params = (is_cancelled, booking_id)
        last_row_id, row_count = self.execute(sql, params)
        return row_count > 0

    # User Story 11: Buchung aktualisieren
    def update_booking(self, booking_id: int, check_in_date: datetime = None, 
                      check_out_date: datetime = None, total_amount: float = None) -> bool:
        updates = []
        params = []
        
        if check_in_date:
            updates.append("Check_in_date = ?")
            params.append(check_in_date)
        if check_out_date:
            updates.append("Check_out_date = ?")
            params.append(check_out_date)
        if total_amount is not None:
            updates.append("Total_amount = ?")
            params.append(total_amount)
        
        if not updates:
            return False
            
        params.append(booking_id)
        sql = f"UPDATE Booking SET {', '.join(updates)} WHERE Booking_id = ?"
        
        last_row_id, row_count = self.execute(sql, tuple(params))
        return row_count > 0

    def delete_booking(self, booking_id: int) -> bool:
        sql = "DELETE FROM Booking WHERE Booking_id = ?"
        params = tuple([booking_id])
        last_row_id, row_count = self.execute(sql, params)
        return row_count > 0

    # Hilfsmethoden
    def _load_room_by_id(self, room_id: int) -> Room | None:
        """Lädt Room-Objekt für Booking"""
        sql = """
        SELECT r.Room_id, r.Hotel_id, r.Room_number, r.Type_id, r.Price_per_night
        FROM Room r
        WHERE r.Room_id = ?
        """
        result = self.fetchone(sql, (room_id,))
        if result:
            room_id, hotel_id, room_number, type_id, price_per_night = result
            # TODO: Vollständiges Room-Objekt mit RoomType laden
            return Room(room_id, hotel_id, room_number, None, price_per_night)
        return None