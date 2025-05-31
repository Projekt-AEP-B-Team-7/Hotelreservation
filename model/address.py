from __future__ import annotations

class Address:
    
    def __init__(self, address_id: int, street: str, city: str, zip_code: str):
        if not address_id:
            raise ValueError("Address ID is required")
        if not isinstance(address_id, int):
            raise ValueError("Address ID must be an integer")
        if not street:
            raise ValueError("Street is required")
        if not isinstance(street, str):
            raise ValueError("Street must be a string")
        if not city:
            raise ValueError("City is required")
        if not isinstance(city, str):
            raise ValueError("City must be a string")
        if not zip_code:
            raise ValueError("Zip Code is required")
        if not isinstance(zip_code, str):
            raise ValueError("Zip Code must be a string")

        self.__address_id: int = address_id
        self.__street: str = street
        self.__city: str = city
        self.__zip_code: str = zip_code

    def __str__(self):
        return f"Street: {self.__street}, Zip code: {self.__zip_code}, City: {self.__city}"

    @property
    def address_id(self) -> int:
        return self.__address_id

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str) -> None:
        if not street:
            raise ValueError("Street is required")
        if not isinstance(street, str):
            raise ValueError("Street must be a string")
        self.__street = street

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str) -> None:
        if not city:
            raise ValueError("City is required")
        if not isinstance(city, str):
            raise ValueError("City must be a string")
        self.__city = city

    @property
    def zip_code(self) -> str:
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, zip_code: str) -> None:
        if not zip_code:
            raise ValueError("Zip Code is required")
        if not isinstance(zip_code, str):
            raise ValueError("Zip Code must be a string")
        self.__zip_code = zip_code