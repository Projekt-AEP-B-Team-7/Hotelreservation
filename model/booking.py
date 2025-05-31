from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.room import Room

class Booking:
    def __init__(self, booking_id: int, guest_id: int, room: Room, 
                 check_in_date: datetime, check_out_date: datetime, 
                 is_cancelled: bool = False, total_amount: float = 0.0):
        if booking_id is not None and not isinstance(booking_id, int):
            raise ValueError("booking_id must be an integer")
        if not isinstance(guest_id, int):
            raise ValueError("guest_id must be an integer")
        if not isinstance(check_in_date, datetime):
            raise ValueError("check_in_date must be a datetime object")
        if not isinstance(check_out_date, datetime):
            raise ValueError("check_out_date must be a datetime object")
        if check_out_date <= check_in_date:
            raise ValueError("check_out_date must be after check_in_date")
        if not isinstance(is_cancelled, bool):
            raise ValueError("is_cancelled must be a boolean")
        if not isinstance(total_amount, (int, float)):
            raise ValueError("total_amount must be a number")
        if total_amount < 0:
            raise ValueError("total_amount cannot be negative")

        self.__booking_id: int = booking_id
        self.__guest_id: int = guest_id
        self.__room: Room = room
        self.__check_in_date: datetime = check_in_date
        self.__check_out_date: datetime = check_out_date
        self.__is_cancelled: bool = is_cancelled
        self.__total_amount: float = float(total_amount)
        self.__booking_date: datetime = datetime.now()

    def __repr__(self):
        return f"Booking(id={self.__booking_id!r}, guest_id={self.__guest_id!r}, room={self.__room!r})"

    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @property
    def guest_id(self) -> int:
        return self.__guest_id

    @property
    def room(self) -> Room:
        return self.__room

    @room.setter
    def room(self, room: Room) -> None:
        from model.room import Room
        if not isinstance(room, Room):
            raise ValueError("room must be an instance of Room")
        self.__room = room

    @property
    def check_in_date(self) -> datetime:
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value: datetime) -> None:
        if not isinstance(value, datetime):
            raise ValueError("check_in_date must be a datetime object")
        self.__check_in_date = value

    @property
    def check_out_date(self) -> datetime:
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value: datetime) -> None:
        if not isinstance(value, datetime):
            raise ValueError("check_out_date must be a datetime object")
        if value <= self.__check_in_date:
            raise ValueError("check_out_date must be after check_in_date")
        self.__check_out_date = value

    @property
    def is_cancelled(self) -> bool:
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("is_cancelled must be a boolean")
        self.__is_cancelled = value

    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError("total_amount must be a number")
        if value < 0:
            raise ValueError("total_amount cannot be negative")
        self.__total_amount = float(value)

    @property
    def booking_date(self) -> datetime:
        return self.__booking_date

    # User Story Support Methods
    def get_nights(self) -> int:
        """User Story 2.1: Berechnung der Nächte für Gesamtpreis"""
        return (self.__check_out_date - self.__check_in_date).days

    def cancel_booking(self) -> None:
        """User Story 6: Buchung stornieren"""
        self.__is_cancelled = True

    def is_active(self) -> bool:
        """User Story 1.4: Prüft ob Buchung aktiv (nicht storniert)"""
        return not self.__is_cancelled

    def overlaps_with(self, check_in: datetime, check_out: datetime) -> bool:
        """User Story 1.4: Prüft Überschneidung mit anderen Buchungen"""
        if self.__is_cancelled:
            return False
        return not (check_out <= self.__check_in_date or check_in >= self.__check_out_date)

    def get_booking_details(self) -> str:
        """User Story 12: Buchungsdetails anzeigen"""
        status = "Cancelled" if self.__is_cancelled else "Active"
        return (
            f"Booking ID: {self.__booking_id}, "
            f"Guest ID: {self.__guest_id}, "
            f"Room: {self.__room.room_number if self.__room else 'N/A'}, "
            f"Check-in: {self.__check_in_date.strftime('%Y-%m-%d')}, "
            f"Check-out: {self.__check_out_date.strftime('%Y-%m-%d')}, "
            f"Nights: {self.get_nights()}, "
            f"Status: {status}, "
            f"Total: {self.__total_amount:.2f} CHF"
        )

    def __str__(self) -> str:
        return f"Booking {self.__booking_id} - {self.get_nights()} nights"