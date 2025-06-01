from __future__ import annotations

from model.address import Address
from model.room import Room

class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address: Address = None):
        if not hotel_id:
            raise ValueError("Hotel ID is required")
        if not isinstance(hotel_id, int):
            raise ValueError("Hotel ID must be an integer")
        if not name:
            raise ValueError("Hotel name is required")
        if not isinstance(name, str):
            raise ValueError("Hotel name must be a string")
        if not isinstance(stars, int):
            raise ValueError("Stars must be an integer")
        if not (1 <= stars <= 5):
            raise ValueError("Stars must be between 1 and 5")
        
        if address is not None and not isinstance(address, Address):
            raise ValueError("Address must be an instance of Address")

        self.__hotel_id: int = hotel_id
        self.__name: str = name
        self.__stars: int = stars
        self.__address: Address = address
        self.__rooms: list[Room] = []

    def __repr__(self):
        return f"Hotel(id={self.__hotel_id!r}, name={self.__name!r}, stars={self.__stars!r})"

    @property
    def hotel_id(self) -> int:
        return self.__hotel_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name:
            raise ValueError("Hotel name is required")
        if not isinstance(name, str):
            raise ValueError("Hotel name must be a string")
        self.__name = name

    @property
    def stars(self) -> int:
        return self.__stars

    @stars.setter
    def stars(self, stars: int) -> None:
        if not isinstance(stars, int):
            raise ValueError("Stars must be an integer")
        if not (1 <= stars <= 5):
            raise ValueError("Stars must be between 1 and 5")
        self.__stars = stars

    @property
    def address(self) -> Address:
        return self.__address

    @address.setter
    def address(self, address: Address) -> None:
        from model.address import Address
        if address is not None and not isinstance(address, Address):
            raise ValueError("Address must be an instance of Address")
        self.__address = address

    @property
    def rooms(self) -> list[Room]:
        return self.__rooms.copy()

    def add_room(self, room: Room) -> None:
        if not room:
            raise ValueError("Room is required")
        if not isinstance(room, Room):
            raise ValueError("Room must be an instance of Room")
        if room not in self.__rooms:
            self.__rooms.append(room)

    def remove_room(self, room: Room) -> None:
        if not room:
            raise ValueError("Room is required")
        if not isinstance(room, Room):
            raise ValueError("Room must be an instance of Room")
        if room in self.__rooms:
            self.__rooms.remove(room)