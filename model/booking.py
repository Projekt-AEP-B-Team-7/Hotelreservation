from booking import Booking

class Booking:
    def __init__(self, booking_id:int, check_in_date:datetime, check_out_date:datetime, is_cancelled:bool, total_amount:float):
        self.booking_id = booking_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.is_cancelled = is_cancelled
        self.total_amount = total_amount

    @property
        def booking_id(self) -> int:
            return self.booking_id

#Frage: "check_in_date : datetime" richtig?
#hier muss man sagen das check in date muss vor check out date sein!!!!
    @property
        def check_in_date(self):
            return self.check_in_date
    
    @street.setter
    def check_in_date(self, check_in_date:datetime) -> None:
        if not check_in_date:
           raise ValueError("Check in date is required.")
        #if not isinstance check_in_date:
         #   raise ValueError("Check in date must be date.")

#hier muss man sagen, dass check out date muss nach check in date sein!!!!
    @property
        def check_out_date(self):
            return self.check_out_date
    
    @street.setter
    def check_out_date(self, check_out_date:datetime) -> None:
        if not check_out_date:
           raise ValueError("Check out date is required.")
        #if not isinstance check_out_date:
         #   raise ValueError("Check out date must be datetime.")

    @property
        def is_cancelled(self):
            return self.is_cancelled
    
    @street.setter
    def is_cancelled(self, is_cancelled:bool) -> None:
        if not is_cancelled:
           raise ValueError("Check out date is required.")
        #if not isinstance check_out_date:
         #   raise ValueError("Check out date must be datetime.")
    
    
    def get_booking_details(self):
        return f"Booking Id: {booking_id}, Check in date: {check_in_date}, Check out date: {check_out_date}, Cancelled: {is_cancelled}, Total amount: {total_amount}"