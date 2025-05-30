class Address:
    def __init__(self, address_id:int, street:str, city:str, zip_code:str):
        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code

    @property
    def address_id(self) -> int:
        return self.__address_id
    
    @property
    def street(self):
        return self.__street
    
    @street.setter
    def street(self, street:str) -> None:
        if not street:
            raise ValueError("Street is required.")
        if not isinstance (street, str):
            raise ValueError("Street must be string.")
    
    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, city:str) -> None:
        if not city:
            raise ValueError("City is required.")
        if not isinstance (city, str):
            raise ValueError("City must be string.")

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, zip_code:int) -> None:
        if not zip_code:
            raise ValueError("Zip code is required.")
        if not isinstance (zip_code, int):
            raise ValueError("Zip code must be integer.")
    
    def get_address_details(self):
        return f"Address Id: {address_id}, Street: {street}, City: {city}, Zip Code: {zip_code}"