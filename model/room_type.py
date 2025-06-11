from __future__ import annotations

class RoomType:
    def __init__(self, type_id: int, description: str, max_guests: int):
        if not type_id:
            raise ValueError("Type ID is required")
        if not isinstance(type_id, int):
            raise ValueError("Type ID must be an integer")
        if not description:
            raise ValueError("Description is required")
        if not isinstance(description, str):
            raise ValueError("Description must be a string")
        if not isinstance(max_guests, int):
            raise ValueError("Max Guests must be an integer")
        if max_guests < 1:
            raise ValueError("Max Guests must be at least 1")

        self.__type_id: int = type_id
        self.__description: str = description
        self.__max_guests: int = max_guests

    def __repr__(self):
        return f"RoomType(id={self.__type_id!r}, Description={self.__description!r}, Max Guests={self.__max_guests!r})"

    @property
    def type_id(self) -> int:
        return self.__type_id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        if not description:
            raise ValueError("Description is required")
        if not isinstance(description, str):
            raise ValueError("Description must be a string")
        self.__description = description

    @property
    def max_guests(self) -> int:
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, max_guests: int) -> None:
        if not isinstance(max_guests, int):
            raise ValueError("Max Guests must be an integer")
        if max_guests < 1:
            raise ValueError("Max Guests must be at least 1")
        self.__max_guests = max_guests