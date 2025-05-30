from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
    
    def create_new_invoice(self, invoice_id:int, booking_id:int, issue_date:str, total_amount:float) -> model.Invoice:
        if invoice_id is None:
            raise ValueError ("Invoice ID is required")
        if booking_id is None:
            raise ValueError ("Booking ID is required")
        if issue_date is None:
            raise ValueError ("Issue Date is required")
        if total_amount is None:
            raise ValueError ("Total Amount is required")
                
    
        sql = """
        INSERT INTO Invoice (invoice_id, booking_id, issue_date, total_amount) VALUES (?, ?, ?, ?)
        """
        params = tuple([invoice_id, booking_id, issue_date, total_amount])

        last_row_id, row_count = self.execute(sql, params)
        return model.Invoice(last_row_id, invoice_id, booking_id, issue_date, total_amount)

    def read_invoice_by_bookingID(self, booking_id) -> model.Invoice:
        
        sql = """
        SELECT * FROM Invoice WHERE Booking_id = ?
        """
        params = tuple([booking_id])
        result = self.fetchone(sql, params)
        if result:
            invoice_id, booking_id, issue_date, total_amount = result
            return model.Invoice(invoice_id, booking_id, issue_date, total_amount)
        else:
            return None
    
    #def update_invoice(self, booking_id) -> model.Invoice:
        if Invoice is None:
            raise ValueError("Invoice cannot be None")

        sql = """
        UPDATE Booking SET is_cancelled = ? WHERE booking_id = ?
        """
        params = tuple([is_cancelled, booking_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_invoice(self, invoice_id) -> model.Invoice:
        if invoice is None:
            raise ValueError("Invoice cannot be None")

        sql = """
        DELETE FROM Invoice WHERE invoice_id = ?
        """
        params = tuple([invoice_id])
        last_row_id, row_count = self.execute(sql, params)


############################################################
from datetime import datetime
from __future__ import annotations
import model
from data_access.base_data_access import BaseDataAccess

class InvoiceDataAccess(BaseDataAccess):

    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_invoice_for_booking(self, booking_id: int, amount: float, is_paid: bool = False) -> model.Invoice:
        if booking_id is None:
            raise ValueError("Booking ID is required")
        if amount is None:
            raise ValueError("Invoice amount is required")

        issue_date = datetime.today().strftime('%Y-%m-%d')

        sql = """
        INSERT INTO Invoice (booking_id, issue_date, amount, is_paid)
        VALUES (?, ?, ?, ?);
        """
        params = (booking_id, issue_date, amount, is_paid)

        last_row_id, _ = self.execute(sql, params)
        return model.Invoice(last_row_id, booking_id, issue_date, amount, is_paid)

