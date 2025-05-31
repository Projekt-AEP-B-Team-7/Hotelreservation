from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from model.address import Address
    from model.booking import Booking

class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, 
                 phone: str = None, date_of_birth: date = None, nationality: str = None, 
                 loyalty_points: int = 0):
        if guest_id is not None and not isinstance(guest_id, int):
            raise ValueError("guest_id must be an integer")
        if not first_name:
            raise ValueError("first_name is required")
        if not isinstance(first_name, str):
            raise ValueError("first_name must be a string")
        if not last_name:
            raise ValueError("last_name is required")
        if not isinstance(last_name, str):
            raise ValueError("last_name must be a string")
        if not email:
            raise ValueError("email is required")
        if not isinstance(email, str):
            raise ValueError("email must be a string")
        if loyalty_points < 0:
            raise ValueError("loyalty_points cannot be negative")

        self.__guest_id: int = guest_id
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__email: str = email
        self.__phone: str = phone
        self.__date_of_birth: date = date_of_birth
        self.__nationality: str = nationality
        self.__loyalty_points: int = loyalty_points
        self.__bookings: list[Booking] = []

    def __repr__(self):
        return f"Guest(id={self.__guest_id!r}, name='{self.__first_name} {self.__last_name}', email='{self.__email}')"

    def __str__(self):
        return f"{self.__first_name} {self.__last_name}"

    @property
    def guest_id(self) -> int:
        return self.__guest_id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        if not first_name:
            raise ValueError("First Name is required")
        if not isinstance(first_name, str):
            raise ValueError("First Name must be a string")
        self.__first_name = first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        if not last_name:
            raise ValueError("Last Name is required")
        if not isinstance(last_name, str):
            raise ValueError("Last Name must be a string")
        self.__last_name = last_name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        if not email:
            raise ValueError("Email is required")
        if not isinstance(email, str):
            raise ValueError("Email must be a string")
        # Basis Email-Validierung
        if "@" not in email or "." not in email:
            raise ValueError("Email must be a valid email address")
        self.__email = email

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str) -> None:
        if phone is not None and not isinstance(phone, str):
            raise ValueError("Phone must be a string")
        self.__phone = phone

    @property
    def date_of_birth(self) -> date:
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: date) -> None:
        if date_of_birth is not None and not isinstance(date_of_birth, date):
            raise ValueError("Date of birth must be a date object")
        self.__date_of_birth = date_of_birth

    @property
    def nationality(self) -> str:
        return self.__nationality

    @nationality.setter
    def nationality(self, nationality: str) -> None:
        if nationality is not None and not isinstance(nationality, str):
            raise ValueError("Nationality must be a string")
        self.__nationality = nationality

    @property
    def loyalty_points(self) -> int:
        return self.__loyalty_points

    @loyalty_points.setter
    def loyalty_points(self, points: int) -> None:
        if not isinstance(points, int):
            raise ValueError("Loyalty points must be an integer")
        if points < 0:
            raise ValueError("Loyalty points cannot be negative")
        self.__loyalty_points = points

    @property
    def bookings(self) -> list[Booking]:
        return self.__bookings.copy()

    # User Story Support Methods
    @property
    def full_name(self) -> str:
        """User Story 4.1, 12: Vollständiger Name für Buchungen"""
        return f"{self.__first_name} {self.__last_name}"

    def add_booking(self, booking: Booking) -> None:
        """User Story 12: Buchung zu Gast hinzufügen"""
        from model.booking import Booking
        if not booking:
            raise ValueError("booking is required")
        if not isinstance(booking, Booking):
            raise ValueError("booking must be an instance of Booking")
        if booking not in self.__bookings:
            self.__bookings.append(booking)

    def remove_booking(self, booking: Booking) -> None:
        """User Story 12: Buchung von Gast entfernen"""
        from model.booking import Booking
        if not booking:
            raise ValueError("booking is required")
        if not isinstance(booking, Booking):
            raise ValueError("booking must be an instance of Booking")
        if booking in self.__bookings:
            self.__bookings.remove(booking)

    def add_loyalty_points(self, points: int) -> None:
        """User Story 15: Treuepunkte hinzufügen"""
        if not isinstance(points, int):
            raise ValueError("Points must be an integer")
        if points < 0:
            raise ValueError("Points cannot be negative")
        self.__loyalty_points += points

    def redeem_loyalty_points(self, points: int) -> bool:
        """User Story 15: Treuepunkte einlösen"""
        if not isinstance(points, int):
            raise ValueError("Points must be an integer")
        if points < 0:
            raise ValueError("Points cannot be negative")
        if points > self.__loyalty_points:
            return False
        self.__loyalty_points -= points
        return True

    def is_frequent_guest(self) -> bool:
        """User Story 15: Prüft ob Gast häufiger Gast ist (für Treuepunkte)"""
        return len([b for b in self.__bookings if not b.is_cancelled]) >= 3

    def get_age(self) -> int:
        """User Story 18: Alter für Demographie-Analyse"""
        if not self.__date_of_birth:
            return None
        from datetime import date
        today = date.today()
        return today.year - self.__date_of_birth.year - ((today.month, today.day) < (self.__date_of_birth.month, self.__date_of_birth.day))

    def get_guest_details(self) -> str:
        """User Story 4.1: Gästedetails für Buchungen"""
        return (
            f"Guest ID: {self.__guest_id}, "
            f"Name: {self.full_name}, "
            f"Email: {self.__email}, "
            f"Phone: {self.__phone or 'N/A'}, "
            f"Loyalty Points: {self.__loyalty_points}"
        )
