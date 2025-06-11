from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date

from model.guest import Guest
from model.hotel import Hotel
from model.booking import Booking

class Review:
    def __init__(self, review_id: int, guest: "Guest", hotel: "Hotel", booking: "Booking", 
                 rating: int, comment: str = None, review_date: date = None):
        if not review_id:
            raise ValueError("Review ID is required")
        if not isinstance(review_id, int):
            raise ValueError("Review ID must be an integer")
        if not guest:
            raise ValueError("Guest is required")
        if not hotel:
            raise ValueError("Hotel is required")
        if not booking:
            raise ValueError("Booking is required")
        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
        if comment is not None and not isinstance(comment, str):
            raise ValueError("Comment must be a string")
        if review_date and not isinstance(review_date, date):
            raise ValueError("Review date must be a date")

        self.__review_id: int = review_id
        self.__guest: "Guest" = guest
        self.__hotel: "Hotel" = hotel
        self.__booking: "Booking" = booking
        self.__rating: int = rating
        self.__comment: str = comment
        self.__review_date: date = review_date or date.today()

    def __repr__(self):
        return f"Review(id={self.__review_id!r}, guest={self.__guest!r}, hotel={self.__hotel!r}, rating={self.__rating!r})"

    @property
    def review_id(self) -> int:
        return self.__review_id

    @property
    def guest(self) -> "Guest":
        return self.__guest

    @guest.setter
    def guest(self, guest: "Guest") -> None:
        if not guest:
            raise ValueError("Guest is required")
        self.__guest = guest

    @property
    def hotel(self) -> "Hotel":
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel: "Hotel") -> None:
        if not hotel:
            raise ValueError("Hotel is required")
        self.__hotel = hotel

    @property
    def booking(self) -> "Booking":
        return self.__booking

    @booking.setter
    def booking(self, booking: "Booking") -> None:
        if not booking:
            raise ValueError("Booking is required")
        self.__booking = booking

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, rating: int) -> None:
        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
        self.__rating = rating

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str) -> None:
        if comment is not None and not isinstance(comment, str):
            raise ValueError("Comment must be a string")
        self.__comment = comment

    @property
    def review_date(self) -> date:
        return self.__review_date

    @review_date.setter
    def review_date(self, review_date: date) -> None:
        if not isinstance(review_date, date):
            raise ValueError("Review date must be a date")
        self.__review_date = review_date
