import model
import data_access
from datetime import datetime

class InvoiceManager:
    def __init__(self) -> None:
        self.__invoice_dal = data_access.InvoiceDataAccess()

    def create_invoice(self, booking_id: int, total_amount: float, is_paid: bool = False) -> model.Invoice:
        # Übergibt heutiges Datum automatisch
        return self.__invoice_dal.create_invoice_for_booking(booking_id, total_amount, is_paid)

    def read_invoice_by_booking_id(self, booking_id: int) -> model.Invoice | None:
        return self.__invoice_dal.read_invoice_by_bookingID(booking_id)

    def update_invoice_paid_status(self, invoice_id: int, is_paid: bool) -> None:
        return self.__invoice_dal.update_invoice_paid_status(invoice_id, is_paid)

    def delete_invoice(self, invoice_id: int) -> None:
        return self.__invoice_dal.delete_invoice(invoice_id)
