import os

import model
import data_access

class InvoiceManager:
    def __init__(self) -> None:
        self.__invoice_dal = data_access.InvoiceDataAccess()

    def create_invoice(self, guest_id:int, room_id:int, check_in_date:str, check_out_date:str, is_cancelled:bool, total_amount: float) -> model.Invoice:
        return self.__invoice_dal.create_new_invoice(name)
    
    def update_invoice(self, is_cancelled: bool) -> model.Invoice:
        return self.__invoice_dal.update_invoice(is_cancelled)
    
    def delete_invoice(self, booking_id) -> model.Invoice:
        return self.__invoice_dal.delete_invoice(invoice_id)
