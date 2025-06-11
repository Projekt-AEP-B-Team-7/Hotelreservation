from model.review import Review
from model.guest import Guest
from model.hotel import Hotel
from model.booking import Booking
from data_access.review_data_access import ReviewDataAccess
from datetime import date

class ReviewManager:
    def __init__(self):
        self.__review_da = ReviewDataAccess()

    def create_review(self, guest: Guest, hotel: Hotel, booking: Booking, 
                     rating: int, comment: str = None) -> Review:
        return self.__review_da.create_new_review(guest, hotel, booking, rating, comment)

    def read_review(self, review_id: int) -> Review:
        return self.__review_da.read_review_by_id(review_id)

    def read_reviews_by_guest(self, guest: Guest) -> list[Review]:
        return self.__review_da.read_reviews_by_guest(guest)

    def read_reviews_by_hotel(self, hotel: Hotel) -> list[Review]:
        return self.__review_da.read_reviews_by_hotel(hotel)

    def read_all_reviews(self) -> list[Review]:
        return self.__review_da.read_all_reviews()

    def check_existing_review(self, guest: Guest, booking: Booking) -> Review | None:
        return self.__review_da.check_existing_review(guest, booking)

    def get_hotel_average_rating(self, hotel: Hotel) -> tuple[float, int]:
        return self.__review_da.get_hotel_average_rating(hotel)

    def can_review_booking(self, booking: Booking) -> bool:
        if booking.is_cancelled:
            return False
        
        today = date.today()
        return booking.check_out_date <= today

    def update_review(self, review: Review) -> None:
        self.__review_da.update_review(review)

    def delete_review(self, review: Review) -> None:
        self.__review_da.delete_review(review)
