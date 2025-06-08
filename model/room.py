from __future__ import annotations

from model.room_type import RoomType
from model.facilities import Facilities

class Room:
    def __init__(self, room_id: int, hotel: "Hotel", room_number: str, room_type: RoomType, price_per_night: float):
        if not room_id:
            raise ValueError("Room ID is required")
        if not isinstance(room_id, int):
            raise ValueError("Room ID must be an integer")
        if not hotel:
            raise ValueError("Hotel is required")
        if not room_number:
            raise ValueError("Room number is required")
        if not isinstance(room_number, str):
            raise ValueError("Room number must be a string")
        if not room_type or not isinstance(room_type, RoomType):
            raise ValueError("Room type must be an instance of RoomType")
        if not isinstance(price_per_night, (int, float)) or price_per_night < 0:
            raise ValueError("Price per night must be a positive number")

        self.__room_id = room_id
        self.__hotel = hotel
        self.__room_number = room_number
        self.__room_type = room_type
        self.__price_per_night = float(price_per_night)
        self.__facilities: list[Facilities] = []

        hotel.add_room(self)

    def __repr__(self):
        return f"Room(id={self.__room_id!r}, number={self.__room_number!r}, type={self.__room_type!r})"

    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def hotel(self) -> "Hotel":
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel: "Hotel") -> None:
        if not hotel:
            raise ValueError("Hotel is required")
        if self.__hotel is not hotel:
            if self.__hotel is not None:
                self.__hotel.remove_room(self)
            self.__hotel = hotel
            if hotel is not None and self not in hotel.rooms:
                hotel.add_room(self)

    @property
    def room_number(self) -> str:
        return self.__room_number

    @room_number.setter
    def room_number(self, room_number: str) -> None:
        if not room_number or not isinstance(room_number, str):
            raise ValueError("Room number must be a string")
        self.__room_number = room_number

    @property
    def room_type(self) -> RoomType:
        return self.__room_type

    @room_type.setter
    def room_type(self, room_type: RoomType) -> None:
        if not room_type or not isinstance(room_type, RoomType):
            raise ValueError("Room type must be an instance of RoomType")
        self.__room_type = room_type

    @property
    def price_per_night(self) -> float:
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, price_per_night: float) -> None:
        if not isinstance(price_per_night, (int, float)) or price_per_night < 0:
            raise ValueError("Price per night must be a positive number")
        self.__price_per_night = float(price_per_night)

    @property
    def facilities(self) -> list[Facilities]:
        return self.__facilities.copy()

    def add_facility(self, facility: Facilities) -> None:
        if not facility or not isinstance(facility, Facilities):
            raise ValueError("Facility must be an instance of Facilities")
        if facility not in self.__facilities:
            self.__facilities.append(facility)

    def remove_facility(self, facility: Facilities) -> None:
        if not facility or not isinstance(facility, Facilities):
            raise ValueError("Facility must be an instance of Facilities")
        if facility in self.__facilities:
            self.__facilities.remove(facility)