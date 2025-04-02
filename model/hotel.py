class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: str):
        self.__hotel_id = hotel_id     
        self.__name = name            
        self.__stars = stars          
        self.__rooms = []              


    def add_rooms(self, room):
        self.__rooms.append(room)

    def get_available_rooms(self):
        return [room for room in self.__rooms if room["available"]]

    def view_rooms(self):
        return self.__rooms