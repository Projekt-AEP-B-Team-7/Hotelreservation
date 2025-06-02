from __future__ import annotations
from model.address import Address

class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, address: Address = None):
        if not guest_id:
            raise ValueError("Guest ID is required")
        if not isinstance(guest_id, int):
            raise ValueError("Guest ID must be an integer")
        if not first_name:
            raise ValueError("First name is required")
        if not isinstance(first_name, str):
            raise ValueError("First name must be a string")
        if not last_name:
            raise ValueError("Last name is required")
        if not isinstance(last_name, str):
            raise ValueError("Last name must be a string")
        if not email:
            raise ValueError("Email is required")
        if not isinstance(email, str):
            raise ValueError("Email must be a string")
        
        if address is not None and not isinstance(address, Address):
            raise ValueError("Address must be an instance of Address")

        self.__guest_id: int = guest_id
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__email: str = email
        self.__address: Address = address

    def __repr__(self):
        return f"Guest(id={self.__guest_id!r}, name={self.__first_name!r} {self.__last_name!r})"

    @property
    def guest_id(self) -> int:
        return self.__guest_id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        if not first_name:
            raise ValueError("First name is required")
        if not isinstance(first_name, str):
            raise ValueError("First name must be a string")
        self.__first_name = first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        if not last_name:
            raise ValueError("Last name is required")
        if not isinstance(last_name, str):
            raise ValueError("Last name must be a string")
        self.__last_name = last_name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        if not email:
            raise ValueError("Email is required")
        if not isinstance(email, str):
            raise ValueError("Email must be a string")
        self.__email = email

    @property
    def address(self) -> Address:
        return self.__address

    @address.setter
    def address(self, address: Address) -> None:
        from model.address import Address
        if address is not None and not isinstance(address, Address):
            raise ValueError("Address must be an instance of Address")
        self.__address = address