import os

from model.hotel import Hotel
from data_access.hotel_data_access import HotelDataAccess 

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_dal = HotelDataAccess()
        self.__address_manager = AddressManager()

    # User Story 3.1: Hotel erstellen
    def create_hotel(self, name: str, stars: int, street: str, city: str, zip_code: str) -> Hotel:
        # Adresse erstellen
        new_address = self.__address_manager.create_address(street, city, zip_code)
        # Hotel mit Adresse erstellen
        return self.__hotel_dal.create_new_hotel(name, stars, new_address.address_id)

    # Basis Read-Methoden
    def read_hotel_by_id(self, hotel_id: int) -> Hotel | None:
        return self.__hotel_dal.read_hotel_by_id(hotel_id)
    
    def read_hotel_by_name(self, name: str) -> Hotel | None:
        return self.__hotel_dal.read_hotel_by_name(name)

    # User Story 1.1: Hotels nach Stadt durchsuchen
    def search_hotels_by_city(self, city: str) -> list[Hotel]:
        return self.__hotel_dal.read_hotels_by_city(city)

    # User Story 1.2: Hotels nach Sternen filtern
    def search_hotels_by_stars(self, min_stars: int) -> list[Hotel]:
        return self.__hotel_dal.read_hotels_by_stars(min_stars)

    # User Story 1.3: Hotels nach Gästezahl
    def search_hotels_by_guests(self, city: str, max_guests: int) -> list[Hotel]:
        return self.__hotel_dal.read_hotels_by_city_and_guests(city, max_guests)

    # User Story 1.4: Hotels nach Verfügbarkeit
    def search_available_hotels(self, city: str, check_in: str, check_out: str) -> list[Hotel]:
        return self.__hotel_dal.read_available_hotels(city, check_in, check_out)

    # User Story 1.5: Kombinierte Hotelsuche
    def search_hotels(self, city: str = None, min_stars: int = None, 
                     max_guests: int = None, check_in: str = None, 
                     check_out: str = None) -> list[Hotel]:
        return self.__hotel_dal.search_hotels_combined(city, min_stars, max_guests, check_in, check_out)

    # User Story 3.3: Hotel aktualisieren
    def update_hotel(self, hotel_id: int, name: str = None, stars: int = None) -> bool:
        return self.__hotel_dal.update_hotel(hotel_id, name, stars)

    # User Story 3.2: Hotel löschen
    def delete_hotel(self, hotel_id: int) -> bool:
        return self.__hotel_dal.delete_hotel(hotel_id)

    # User Story 8: Alle Hotels für Admin
    def get_all_hotels(self) -> list[Hotel]:
        return self.__hotel_dal.read_all_hotels()

    # User Story Hilfsmethoden
    def get_hotels_in_city_with_stars(self, city: str, min_stars: int) -> list[Hotel]:
        """User Story 1.5: Kombiniert Stadt + Sterne"""
        return self.__hotel_dal.read_hotels_by_city_and_stars(city, min_stars)