from model.room import Room
from model.address import Address

class Hotel:
    def __init__(self, hotel_id: int, name: str, star: str, address: str):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__star = star
        self.__address = address
        self.__rooms = []

    @property
    def hotel_id(self) -> int:
        return self.__hotel_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def star(self) -> str:
        return self.__star

    @property
    def address(self) -> str:
        return self.__address

    def __repr__(self):
        return f"Hotel: {self.name}, Stars: {self.star}, Address: {self.address.city}, {self.address.street}, {self.address.zip_code}"

   # def add_room(self, room: Room):
#        self.__rooms.append(room)

#    def get_available_rooms(self) -> list:
 #       return [room for room in self.__rooms if room.is_available]

#    def view_rooms(self) -> list:
 #       return self.__rooms

   # def sort_rooms_by_price(self) -> list:
   #     return sorted(self.__rooms, key=lambda r: r.price_per_night)

