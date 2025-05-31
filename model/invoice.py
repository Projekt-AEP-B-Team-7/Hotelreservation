from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from model.booking import Booking

class Invoice:
    def __init__(self, invoice_id: int, booking: Booking, issue_date: date, total_amount: float):
        if not invoice_id:
            raise ValueError("Invoice ID is required")
        if not isinstance(invoice_id, int):
            raise ValueError("Invoice ID must be an integer")
        if not booking:
            raise ValueError("Booking is required")
        if not isinstance(booking, Booking):
            raise ValueError("Booking must be an instance of Booking")
        if not issue_date:
            raise ValueError("Issue date is required")
        if not isinstance(issue_date, date):
            raise ValueError("Issue date must be a date")
        if not isinstance(total_amount, (int, float)):
            raise ValueError("Total amount must be a number")
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

        self.__invoice_id: int = invoice_id
        self.__booking: Booking = booking
        self.__issue_date: date = issue_date
        self.__total_amount: float = float(total_amount)

    def __repr__(self):
        return f"Invoice(id={self.__invoice_id!r}, booking={self.__booking!r}, amount={self.__total_amount!r})"

    @property
    def invoice_id(self) -> int:
        return self.__invoice_id

    @property
    def booking(self) -> Booking:
        return self.__booking

    @booking.setter
    def booking(self, booking: Booking) -> None:
        from model.booking import Booking
        if not booking:
            raise ValueError("Booking is required")
        if not isinstance(booking, Booking):
            raise ValueError("Booking must be an instance of Booking")
        self.__booking = booking

    @property
    def issue_date(self) -> date:
        return self.__issue_date

    @issue_date.setter
    def issue_date(self, issue_date: date) -> None:
        if not issue_date:
            raise ValueError("Issue date is required")
        if not isinstance(issue_date, date):
            raise ValueError("Issue date must be a date")
        self.__issue_date = issue_date

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