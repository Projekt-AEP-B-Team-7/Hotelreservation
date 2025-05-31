from model.address import Address
from data_access.address_data_access import AddressDataAccess

class AddressManager:
    def __init__(self) -> None:
        self.__address_dal = AddressDataAccess()

    def create_address(self, street: str, city: str, zip_code: str) -> Address:
        """Erstellt eine neue Adresse"""
        return self.__address_dal.create_new_address(street, city, zip_code)

    def read_address_by_id(self, address_id: int) -> Address | None:
        """Liest eine Adresse anhand der ID"""
        return self.__address_dal.read_address_by_id(address_id)

    def read_addresses_by_city(self, city: str) -> list[Address]:
        """User Story 1.1: Alle Adressen in einer Stadt"""
        return self.__address_dal.read_addresses_by_city(city)

    def update_address(self, address_id: int, street: str = None, 
                      city: str = None, zip_code: str = None) -> bool:
        """Aktualisiert eine Adresse"""
        return self.__address_dal.update_address(address_id, street, city, zip_code)

    def delete_address(self, address_id: int) -> bool:
        """Löscht eine Adresse"""
        return self.__address_dal.delete_address(address_id)

    def get_all_addresses(self) -> list[Address]:
        """Alle Adressen für Admin"""
        return self.__address_dal.read_all_addresses()

    def find_cities(self) -> list[str]:
        """User Story 1.1: Alle verfügbaren Städte finden"""
        addresses = self.__address_dal.read_all_addresses()
        cities = list(set(addr.city for addr in addresses))
        return sorted(cities)