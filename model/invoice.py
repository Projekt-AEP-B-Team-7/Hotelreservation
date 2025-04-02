from datetime import date

class Invoice:
    def __init__(self, invoice_id: int, issue_date: date, total_amount: float):
        self._invoice_id = invoice_id
        self._issue_date = issue_date
        self._total_amount = total_amount

    @property
    def invoice_id(self) -> int:
        return self._invoice_id

    @property
    def issue_date(self) -> date:
        return self._issue_date

    @property
    def total_amount(self) -> float:
        return self._total_amount

    def generate_pdf(self) -> None:
        # Platzhalter für PDF-Erzeugung
        print(f"Invoice {self._invoice_id} was generated as a PDF.")

    def send_to_guest(self) -> None:
        # Platzhalter für Sende-Logik
        print(f"Invoice {self._invoice_id} has been sent to guest.")