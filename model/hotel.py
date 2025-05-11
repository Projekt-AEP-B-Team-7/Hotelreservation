class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: str):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__rooms = []

    @property
    def hotel_id(self) -> int:
        return self.__hotel_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def stars(self) -> str:
        return self.__stars

    def add_room(self, room: Room):
        self.__rooms.append(room)

    def get_available_rooms(self) -> list:
        return [room for room in self.__rooms if room.is_available]

    def view_rooms(self) -> list:
        return self.__rooms

    def sort_rooms_by_price(self) -> list:
        return sorted(self.__rooms, key=lambda r: r.price_per_night)

    def find_rooms_by_max_price(self, max_price: float) -> list:
        return [room for room in self.__rooms if room.price_per_night <= max_price]
