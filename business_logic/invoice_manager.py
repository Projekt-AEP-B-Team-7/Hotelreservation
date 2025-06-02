import model
import data_access
from datetime import date, datetime
from model.invoice import Invoice
from model.booking import Booking
from model.guest import Guest
from data_access.invoice_data_access import InvoiceDataAccess


class InvoiceManager:
    def __init__(self):
        self.__invoice_da = InvoiceDataAccess()

    def create_invoice(self, booking: Booking, issue_date: date, total_amount: float) -> Invoice:
        return self.__invoice_da.create_new_invoice(booking, issue_date, total_amount)

    def read_invoice(self, invoice_id: int) -> Invoice:
        return self.__invoice_da.read_invoice_by_id(invoice_id)

    def read_invoice_by_booking(self, booking: Booking) -> Invoice:
        return self.__invoice_da.read_invoice_by_booking(booking)

    def read_invoices_by_guest(self, guest: Guest) -> list[Invoice]:
        return self.__invoice_da.read_invoices_by_guest(guest)

    def read_all_invoices(self) -> list[Invoice]:
        return self.__invoice_da.read_all_invoices()

    def update_invoice(self, invoice: Invoice) -> None:
        self.__invoice_da.update_invoice(invoice)

    def delete_invoice(self, invoice: Invoice) -> None:
        self.__invoice_da.delete_invoice(invoice)