import os

from model.hotel import Hotel
from model.address import Address
from data_access.hotel_data_access import HotelDataAccess

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = HotelDataAccess()

    def create_hotel(self, name: str, stars: int, address: Address = None) -> Hotel:
        return self.__hotel_da.create_new_hotel(name, stars, address)

    def read_hotel(self, hotel_id: int) -> Hotel:
        return self.__hotel_da.read_hotel_by_id(hotel_id)

    def read_hotels_by_city(self, city: str) -> list[Hotel]:
        return self.__hotel_da.read_hotels_by_city(city)

    def read_hotels_by_stars(self, min_stars: int) -> list[Hotel]:
        return self.__hotel_da.read_hotels_by_stars(min_stars)

    def read_hotels_by_city_and_stars(self, city: str, min_stars: int) -> list[Hotel]:
        return self.__hotel_da.read_hotels_by_city_and_stars(city, min_stars)

    def read_hotels_by_guest_capacity(self, city: str, max_guests: int) -> list[Hotel]:
        return self.__hotel_da.read_hotels_by_guest_capacity(city, max_guests)

    def read_available_hotels(self, city: str, check_in_date: str, check_out_date: str) -> list[Hotel]:
        return self.__hotel_da.read_available_hotels(city, check_in_date, check_out_date)

    def read_all_hotels(self) -> list[Hotel]:
        return self.__hotel_da.read_all_hotels()

    def update_hotel(self, hotel: Hotel) -> None:
        self.__hotel_da.update_hotel(hotel)

    def delete_hotel(self, hotel: Hotel) -> None:
        self.__hotel_da.delete_hotel(hotel)