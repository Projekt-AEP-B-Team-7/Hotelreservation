import os

from model.hotel import Hotel
from data_access.hotel_data_access import HotelDataAccess 

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_dal = HotelDataAccess()

    def create_hotel(self, name: str, city: str, stars: int) -> Hotel:
        return self.__hotel_dal.create_hotel(name, city, stars)

    def read_hotel_by_id(self, hotel_id: int) -> Hotel | None:
        return self.__hotel_dal.read_hotel_by_id(hotel_id)
    
    def read_hotel_by_city(self, city: str) -> list[Hotel]:
        return self.__hotel_dal.read_hotel_by_city(city)

    def read_hotels_by_city_and_stars(self, city: str, stars: int) -> list[Hotel]:
        return self.__hotel_dal.read_hotels_by_city_and_stars(city, stars)

    def update_hotel(self, hotel_id: int, name: str, city: str, stars: int) -> bool:
        return self.__hotel_dal.update_hotel(hotel_id, name, city, stars)

    def delete_hotel(self, hotel_id: int) -> bool:
        return self.__hotel_dal.delete_hotel(hotel_id)
