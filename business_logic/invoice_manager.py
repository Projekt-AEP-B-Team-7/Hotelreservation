import model
import data_access
from datetime import datetime

class InvoiceManager:
    def __init__(self):
        self.__invoice_da = data_access.InvoiceDataAccess()

    def create_invoice(self, booking: model.Booking, issue_date: date, total_amount: float) -> model.Invoice:
        return self.__invoice_da.create_new_invoice(booking, issue_date, total_amount)

    def read_invoice(self, invoice_id: int) -> model.Invoice:
        return self.__invoice_da.read_invoice_by_id(invoice_id)

    def read_invoice_by_booking(self, booking: model.Booking) -> model.Invoice:
        return self.__invoice_da.read_invoice_by_booking(booking)

    def read_invoices_by_guest(self, guest: model.Guest) -> list[model.Invoice]:
        return self.__invoice_da.read_invoices_by_guest(guest)

    def read_all_invoices(self) -> list[model.Invoice]:
        return self.__invoice_da.read_all_invoices()

    def update_invoice(self, invoice: model.Invoice) -> None:
        self.__invoice_da.update_invoice(invoice)

    def delete_invoice(self, invoice: model.Invoice) -> None:
        self.__invoice_da.delete_invoice(invoice)