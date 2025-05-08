from address import address

class Guest:
    def __init__(self, guest_id:int, first_name:str, last_name:str, email:str):
        self.__guest_id = guest_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def guest_id(self) -> int:
        return self.__guest_id


    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name : str):
        if not first_name:
            raise ValueError ("First Name required")
        if not isinstance(first_name , str):
             raise TypeError("First Name must be a string")

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name : str):
        if not last_name:
            raise valueerror ("Last Name required")
        if not isinstance(last_name , str):
             raise TypeError("Last Name must be a string")

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email : str):
        if not email:
            raise valueerror ("email required")
        if not isinstance(email , str):
             raise TypeError("email must be a string")

    def get_guest_details(self):
        return f"Guest Id: {guest_id}, First Name: {first_name}, Last Name: {last_name}, E-Mail: {email}"