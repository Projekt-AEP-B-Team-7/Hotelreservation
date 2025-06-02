from __future__ import annotations
from datetime import date, datetime
from model.guest import Guest
from model.room import Room

class Booking:
    def __init__(self, booking_id: int, guest: Guest, room: Room, check_in_date: date, check_out_date: date, is_cancelled: bool = False, total_amount: float = 0.0):
        if not booking_id:
            raise ValueError("Booking ID is required")
        if not isinstance(booking_id, int):
            raise ValueError("Booking ID must be an integer")
        if not guest:
            raise ValueError("Guest is required")
        if not isinstance(guest, Guest):
            raise ValueError("Guest must be an instance of Guest")
        if not room:
            raise ValueError("Room is required")
        if not isinstance(room, Room):
            raise ValueError("Room must be an instance of Room")
        if not check_in_date:
            raise ValueError("Check in date is required")
        if not isinstance(check_in_date, date):
            raise ValueError("Check in date must be a date")
        if not check_out_date:
            raise ValueError("Check out date is required")
        if not isinstance(check_out_date, date):
            raise ValueError("Check out date must be a date")
        if check_out_date <= check_in_date:
            raise ValueError("Check out date must be after Check in Date")
        if not isinstance(is_cancelled, bool):
            raise ValueError("Is cancelled must be a boolean")
        if not isinstance(total_amount, (int, float)):
            raise ValueError("Total amount must be a number")
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        self.__booking_id: int = booking_id
        self.__guest: Guest = guest
        self.__room: Room = room
        self.__check_in_date: date = check_in_date
        self.__check_out_date: date = check_out_date
        self.__is_cancelled: bool = is_cancelled
        self.__total_amount: float = float(total_amount)

    def __repr__(self):
        return f"Booking(id={self.__booking_id!r}, guest={self.__guest!r}, room={self.__room!r})"

    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @property
    def guest(self) -> Guest:
        return self.__guest

    @guest.setter
    def guest(self, guest: Guest) -> None:
        from model.guest import Guest
        if not guest:
            raise ValueError("Guest is required")
        if not isinstance(guest, Guest):
            raise ValueError("Guest must be an instance of Guest")
        self.__guest = guest

    @property
    def room(self) -> Room:
        return self.__room

    @room.setter
    def room(self, room: Room) -> None:
        from model.room import Room
        if not room:
            raise ValueError("Room is required")
        if not isinstance(room, Room):
            raise ValueError("Room must be an instance of Room")
        self.__room = room

    @property
    def check_in_date(self) -> date:
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, check_in_date: date) -> None:
        if not check_in_date:
            raise ValueError("Check in date is required")
        if not isinstance(check_in_date, date):
            raise ValueError("Check in date must be a date")
        self.__check_in_date = check_in_date

    @property
    def check_out_date(self) -> date:
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, check_out_date: date) -> None:
        if not check_out_date:
            raise ValueError("Check out date is required")
        if not isinstance(check_out_date, date):
            raise ValueError("Check out date must be a date")
        if check_out_date <= self.__check_in_date:
            raise ValueError("Check out date must be after check in date")
        self.__check_out_date = check_out_date

    @property
    def is_cancelled(self) -> bool:
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, is_cancelled: bool) -> None:
        if not isinstance(is_cancelled, bool):
            raise ValueError("Is cancelled must be a boolean")
        self.__is_cancelled = is_cancelled

    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, total_amount: float) -> None:
        if not isinstance(total_amount, (int, float)):
            raise ValueError("Total amount must be a number")
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")
        self.__total_amount = float(total_amount)