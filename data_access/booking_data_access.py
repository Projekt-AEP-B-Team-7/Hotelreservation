from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
    
    def create_new_booking(self, guest_id:int, room_id:int, check_in_date:str, check_out_date:str, is_cancelled:bool, total_amount: float) -> model.Booking:
        if guest_id is None:
            raise ValueError ("Guest ID is required")
        if room_id is None:
            raise ValueError ("Room ID is required")
        if check_in_date is None:
            raise ValueError ("Check in date is required")
        if check_out_date is None:
            raise ValueError ("Check out date is required")
        if is_cancelled is None:
            raise ValueError ("Cancellation must be true or false")
        if total_amount is None:
            raise ValueError ("Total amount is required")            
    
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, total_amount) VALUES (?, ?, ?, ?, ?)
        """
        params = tuple([guest_id, room_id, check_in_date, check_out_date, total_amount])

        last_row_id, row_count = self.execute(sql, params)
        return model.Booking(last_row_id, guest_id, room_id, check_in_date, check_out_date, total_amount)

    def read_booking_by_guestId(self, guest_id) -> model.Booking:
        
        sql = """
        SELECT * FROM Booking WHERE guest_id = ?
        """
        params = tuple([guest_id])
        result = self.fetchone(sql, params)
        if result:
            guest_id, room_id, check_in_date, check_in_date, is_cancelled, total_amount = result
            return model.Booking(guest_id, room_id, check_in_date, check_in_date, is_cancelled, total_amount)
        else:
            return None
    
    def update_booking(self, is_cancelled: bool) -> model.Booking:
        if booking is None:
            raise ValueError("Booking cannot be None")

        sql = """
        UPDATE Booking SET is_cancelled = ? WHERE booking_id = ?
        """
        params = tuple([is_cancelled, booking_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_booking(self, booking_id) -> model.Booking:
        if booking is None:
            raise ValueError("Booking cannot be None")

        sql = """
        DELETE FROM Booking WHERE booking_id = ?
        """
        params = tuple([booking_id])
        last_row_id, row_count = self.execute(sql, params)

    def read_all_bookings(self, booking_id) -> model.Booking:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount
        FROM Booking;
        """
        rows = self.fetchall(sql)
        return [model.Booking(*row) for row in rows]

#########################################################
def get_room_by_id(self, room_id: int) -> model.Room | None:
    if room_id is None:
        raise ValueError("Room ID is required.")

    sql = """
    SELECT room_id, hotel_id, room_number, type_id, price_per_night
    FROM Room
    WHERE room_id = ?;
    """
    result = self.fetchone(sql, (room_id,))
    if result:
        room_id, hotel_id, room_number, type_id, price_per_night = result
        return model.Room(room_id, hotel_id, room_number, type_id, price_per_night)
    return None
