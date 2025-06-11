from __future__ import annotations
from datetime import date
from model.review import Review
from model.guest import Guest
from model.hotel import Hotel
from model.booking import Booking
from model.room import Room
from model.room_type import RoomType
from model.address import Address
from data_access.base_data_access import BaseDataAccess

class ReviewDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_review(self, guest: Guest, hotel: Hotel, booking: Booking, 
                         rating: int, comment: str = None) -> Review:
        if guest is None:
            raise ValueError("Guest is required")
        if hotel is None:
            raise ValueError("Hotel is required")
        if booking is None:
            raise ValueError("Booking is required")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        sql = """
        INSERT INTO Review (guest_id, hotel_id, booking_id, rating, comment, review_date) 
        VALUES (?, ?, ?, ?, ?, ?)
        """
        review_date = date.today()
        params = (guest.guest_id, hotel.hotel_id, booking.booking_id, rating, comment, review_date)
        last_row_id, row_count = self.execute(sql, params)
        return Review(last_row_id, guest, hotel, booking, rating, comment, review_date)

    def read_review_by_id(self, review_id: int) -> Review | None:
        if review_id is None:
            raise ValueError("Review ID is required")

        sql = """
        SELECT Review.review_id, Review.rating, Review.comment, Review.review_date,
               Guest.guest_id, Guest.first_name, Guest.last_name, Guest.email, Guest.phone_number,
               Hotel.hotel_id, Hotel.name AS hotel_name, Hotel.stars,
               Booking.booking_id, Booking.check_in_date, Booking.check_out_date, Booking.total_amount,
               Room.room_id, Room.room_number, Room.price_per_night,
               Room_Type.type_id, Room_Type.description, Room_Type.max_guests,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Review
        JOIN Guest ON Review.guest_id = Guest.guest_id
        JOIN Hotel ON Review.hotel_id = Hotel.hotel_id
        JOIN Booking ON Review.booking_id = Booking.booking_id
        JOIN Room ON Booking.room_id = Room.room_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        LEFT JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Review.review_id = ?
        """
        params = tuple([review_id])
        result = self.fetchone(sql, params)
        
        if result:
            (review_id, rating, comment, review_date,
             guest_id, first_name, last_name, email, phone_number,
             hotel_id, hotel_name, hotel_stars,
             booking_id, check_in_date, check_out_date, total_amount,
             room_id, room_number, price_per_night,
             type_id, type_description, max_guests,
             address_id, street, city, zip_code) = result
            
            address = None
            if address_id:
                address = Address(address_id, street, city, zip_code)
            
            guest = Guest(guest_id, first_name, last_name, email, phone_number, None)
            hotel = Hotel(hotel_id, hotel_name, hotel_stars, address)
            room_type = RoomType(type_id, type_description, max_guests)
            room = Room(room_id, hotel, room_number, room_type, price_per_night)
            booking = Booking(booking_id, guest, room, check_in_date, check_out_date, False, total_amount)
            
            return Review(review_id, guest, hotel, booking, rating, comment, review_date)
        else:
            return None

    def read_reviews_by_guest(self, guest: Guest) -> list[Review]:
        if guest is None:
            raise ValueError("Guest cannot be None")

        sql = """
        SELECT Review.review_id, Review.rating, Review.comment, Review.review_date,
               Hotel.hotel_id, Hotel.name AS hotel_name, Hotel.stars,
               Booking.booking_id, Booking.check_in_date, Booking.check_out_date,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Review
        JOIN Hotel ON Review.hotel_id = Hotel.hotel_id
        JOIN Booking ON Review.booking_id = Booking.booking_id
        LEFT JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Review.guest_id = ?
        ORDER BY Review.review_date DESC
        """
        params = tuple([guest.guest_id])
        reviews = self.fetchall(sql, params)
        
        result = []
        for (review_id, rating, comment, review_date,
             hotel_id, hotel_name, hotel_stars,
             booking_id, check_in_date, check_out_date,
             address_id, street, city, zip_code) in reviews:
            
            address = None
            if address_id:
                address = Address(address_id, street, city, zip_code)
            
            hotel = Hotel(hotel_id, hotel_name, hotel_stars, address)
            booking = Booking(booking_id, guest, None, check_in_date, check_out_date, False, 0.0)
            result.append(Review(review_id, guest, hotel, booking, rating, comment, review_date))
        
        return result

    def read_reviews_by_hotel(self, hotel: Hotel) -> list[Review]:
        if hotel is None:
            raise ValueError("Hotel cannot be None")

        sql = """
        SELECT Review.review_id, Review.rating, Review.comment, Review.review_date,
               Guest.guest_id, Guest.first_name, Guest.last_name, Guest.email, Guest.phone_number,
               Booking.booking_id, Booking.check_in_date, Booking.check_out_date
        FROM Review
        JOIN Guest ON Review.guest_id = Guest.guest_id
        JOIN Booking ON Review.booking_id = Booking.booking_id
        WHERE Review.hotel_id = ?
        ORDER BY Review.review_date DESC
        """
        params = tuple([hotel.hotel_id])
        reviews = self.fetchall(sql, params)
        
        result = []
        for (review_id, rating, comment, review_date,
             guest_id, first_name, last_name, email, phone_number,
             booking_id, check_in_date, check_out_date) in reviews:
            
            guest = Guest(guest_id, first_name, last_name, email, phone_number, None)
            booking = Booking(booking_id, guest, None, check_in_date, check_out_date, False, 0.0)
            result.append(Review(review_id, guest, hotel, booking, rating, comment, review_date))
        
        return result

    def read_all_reviews(self) -> list[Review]:
        sql = """
        SELECT Review.review_id, Review.rating, Review.comment, Review.review_date,
               Guest.guest_id, Guest.first_name, Guest.last_name, Guest.email, Guest.phone_number,
               Hotel.hotel_id, Hotel.name AS hotel_name, Hotel.stars,
               Booking.booking_id, Booking.check_in_date, Booking.check_out_date,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Review
        JOIN Guest ON Review.guest_id = Guest.guest_id
        JOIN Hotel ON Review.hotel_id = Hotel.hotel_id
        JOIN Booking ON Review.booking_id = Booking.booking_id
        LEFT JOIN Address ON Hotel.address_id = Address.address_id
        ORDER BY Review.review_date DESC
        """
        reviews = self.fetchall(sql)
        
        result = []
        for (review_id, rating, comment, review_date,
             guest_id, first_name, last_name, email, phone_number,
             hotel_id, hotel_name, hotel_stars,
             booking_id, check_in_date, check_out_date,
             address_id, street, city, zip_code) in reviews:
            
            address = None
            if address_id:
                address = Address(address_id, street, city, zip_code)
            
            guest = Guest(guest_id, first_name, last_name, email, phone_number, None)
            hotel = Hotel(hotel_id, hotel_name, hotel_stars, address)
            booking = Booking(booking_id, guest, None, check_in_date, check_out_date, False, 0.0)
            result.append(Review(review_id, guest, hotel, booking, rating, comment, review_date))
        
        return result

    def check_existing_review(self, guest: Guest, booking: Booking) -> Review | None:
        sql = """
        SELECT review_id FROM Review WHERE guest_id = ? AND booking_id = ?
        """
        params = tuple([guest.guest_id, booking.booking_id])
        result = self.fetchone(sql, params)
        
        if result:
            return self.read_review_by_id(result[0])
        return None

    def get_hotel_average_rating(self, hotel: Hotel) -> tuple[float, int]:
        sql = """
        SELECT AVG(rating), COUNT(*) FROM Review WHERE hotel_id = ?
        """
        params = tuple([hotel.hotel_id])
        result = self.fetchone(sql, params)
        
        if result and result[0] is not None:
            return round(float(result[0]), 1), int(result[1])
        return 0.0, 0

    def update_review(self, review: Review) -> None:
        if review is None:
            raise ValueError("Review cannot be None")

        sql = """
        UPDATE Review SET rating = ?, comment = ? WHERE review_id = ?
        """
        params = tuple([review.rating, review.comment, review.review_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_review(self, review: Review) -> None:
        if review is None:
            raise ValueError("Review cannot be None")

        sql = """
        DELETE FROM Review WHERE review_id = ?
        """
        params = tuple([review.review_id])
        last_row_id, row_count = self.execute(sql, params)
