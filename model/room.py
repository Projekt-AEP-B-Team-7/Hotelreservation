class Room:
    def __init__(self, room_id: int, room_no: str, price_per_night: float):
        self.__room_id = room_id               
        self.__room_no = room_no               
        self.__price_per_night = price_per_night  
        self.__available = True                

    @property
    def room_id(self) -> room_id:
        return self.__room_id

    @property
    def room_no = room_no 
        return self.__room_no
    
    @property
    def is_available(self) -> bool:
        return self.__available

    @property
    def assign_booking(self):
        return self.__available = False

    @property
    def __str__(self):
        return f"Zimmer {self.__room_no} | Preis/Nacht: {self.__price_per_night} | Verfügbar: {self.__available}"
