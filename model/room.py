from model.room_type import RoomType

class Room:
    def __init__(self, room_id: int, room_number: str, room_type: str, 
                 max_guests: int, price_per_night: float, hotel: Hotel = None):
        if not room_id:
            raise ValueError("room_id is required")
        if not isinstance(room_id, int):
            raise ValueError("room_id must be an integer")
        if not room_number:
            raise ValueError("room_number is required")
        if not isinstance(room_number, str):
            raise ValueError("room_number must be a string")
        if not room_type:
            raise ValueError("room_type is required")
        if not isinstance(room_type, str):
            raise ValueError("room_type must be a string")
        if not isinstance(max_guests, int):
            raise ValueError("max_guests must be an integer")
        if max_guests < 1:
            raise ValueError("max_guests must be at least 1")
        if not isinstance(price_per_night, (int, float)):
            raise ValueError("price_per_night must be a number")
        if price_per_night < 0:
            raise ValueError("price_per_night cannot be negative")

        self.__room_id: int = room_id
        self.__room_number: str = room_number
        self.__room_type: str = room_type
        self.__max_guests: int = max_guests
        self.__price_per_night: float = float(price_per_night)
        self.__hotel: Hotel = hotel
        if hotel is not None:
            hotel.add_room(self)
        self.__bookings: list[Booking] = []

    def __repr__(self):
        return f"Room(id={self.__room_id!r}, number={self.__room_number!r}, type={self.__room_type!r})"

    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def room_number(self) -> str:
        return self.__room_number

    @room_number.setter
    def room_number(self, room_number: str) -> None:
        if not room_number:
            raise ValueError("room_number is required")
        if not isinstance(room_number, str):
            raise ValueError("room_number must be a string")
        self.__room_number = room_number

    @property
    def room_type(self) -> str:
        return self.__room_type

    @room_type.setter
    def room_type(self, room_type: str) -> None:
        if not room_type:
            raise ValueError("room_type is required")
        if not isinstance(room_type, str):
            raise ValueError("room_type must be a string")
        self.__room_type = room_type

    @property
    def max_guests(self) -> int:
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, max_guests: int) -> None:
        if not isinstance(max_guests, int):
            raise ValueError("max_guests must be an integer")
        if max_guests < 1:
            raise ValueError("max_guests must be at least 1")
        self.__max_guests = max_guests

    @property
    def price_per_night(self) -> float:
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, price_per_night: float) -> None:
        if not isinstance(price_per_night, (int, float)):
            raise ValueError("price_per_night must be a number")
        if price_per_night < 0:
            raise ValueError("price_per_night cannot be negative")
        self.__price_per_night = float(price_per_night)

    @property
    def hotel(self) -> Hotel:
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel: Hotel) -> None:
        if hotel is not None and not isinstance(hotel, Hotel):
            raise ValueError("hotel must be an instance of Hotel")
        if self.__hotel is not hotel:
            if self.__hotel is not None:
                self.__hotel.remove_room(self)
            self.__hotel = hotel
            if hotel is not None and self not in hotel.rooms:
                hotel.add_room(self)