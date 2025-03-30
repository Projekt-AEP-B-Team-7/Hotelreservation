from address import address

class Guest:
    def __init__(self, guest_id:int, first_name:str, last_name:str, email:str):
        self.guest_id = guest_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email