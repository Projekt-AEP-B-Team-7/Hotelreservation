class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address: Address = None):
        if not hotel_id:
            raise ValueError("hotel_id is required")
        if not isinstance(hotel_id, int):
            raise ValueError("hotel_id must be an integer")
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not isinstance(stars, int):
            raise ValueError("stars must be an integer")
        if not (1 <= stars <= 5):
            raise ValueError("stars must be between 1 and 5")

        self.__hotel_id: int = hotel_id
        self.__name: str = name
        self.__stars: int = stars
        self.__address: Address = address
        self.__rooms: list[Room] = []
        self.__bookings: list[Booking] = []

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
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        self.__name = name

    @property
    def stars(self) -> int:
        return self.__stars

    @stars.setter
    def stars(self, stars: int) -> None:
        if not isinstance(stars, int):
            raise ValueError("stars must be an integer")
        if not (1 <= stars <= 5):
            raise ValueError("stars must be between 1 and 5")
        self.__stars = stars

    @property
    def address(self) -> Address:
        return self.__address

    @address.setter
    def address(self, address: Address) -> None:
        from model.address import Address
        if address is not None and not isinstance(address, Address):
            raise ValueError("address must be an instance of Address")
        self.__address = address

    @property
    def rooms(self) -> list[Room]:
        return self.__rooms.copy()

    @property
    def bookings(self) -> list[Booking]:
        return self.__bookings.copy()

    def add_room(self, room: Room) -> None:
        from model.room import Room
        if not room:
            raise ValueError("room is required")
        if not isinstance(room, Room):
            raise ValueError("room must be an instance of Room")
        if room not in self.__rooms:
            self.__rooms.append(room)
            if room.hotel is not self:
                room.hotel = self

    def remove_room(self, room: Room) -> None:
        from model.room import Room
        if not room:
            raise ValueError("room is required")
        if not isinstance(room, Room):
            raise ValueError("room must be an instance of Room")
        if room in self.__rooms:
            self.__rooms.remove(room)
            room.hotel = None

    def add_booking(self, booking: Booking) -> None:
        from model.booking import Booking
        if not booking:
            raise ValueError("booking is required")
        if not isinstance(booking, Booking):
            raise ValueError("booking must be an instance of Booking")
        if booking not in self.__bookings:
            self.__bookings.append(booking)

    def remove_booking(self, booking: Booking) -> None:
        from model.booking import Booking
        if not booking:
            raise ValueError("booking is required")
        if not isinstance(booking, Booking):
            raise ValueError("booking must be an instance of Booking")
        if booking in self.__bookings:
            self.__bookings.remove(booking)

    # User Story Support Methods
    def matches_stars(self, min_stars: int) -> bool:
        """User Story 1.2: Hotels nach Sternen filtern"""
        return self.__stars >= min_stars

    def get_city(self) -> str:
        """User Story 1.1: Stadt für Hotelsuche"""
        return self.__address.city if self.__address else ""

    def get_hotel_info(self) -> str:
        """User Story 1.6: Hotelinformationen anzeigen"""
        address_str = str(self.__address) if self.__address else "No address"
        return f"Name: {self.__name}, Address: {address_str}, Stars: {self.__stars}"