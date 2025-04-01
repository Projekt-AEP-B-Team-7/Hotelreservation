class RoomType:
    def __init__(self, room_type_id: int, description: str, max_guests: int):
        self._room_type_id = room_type_id
        self._description = description
        self._max_guests = max_guests

    @property
    def room_type_id(self) -> int:
        return self._room_type_id

    @property
    def description(self) -> str:
        return self._description

    @property
    def max_guests(self) -> int:
        return self._max_guests

