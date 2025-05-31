from __future__ import annotations

from model.hotel import Hotel
from model.address import Address
from model.room import Room
from model.room_type import RoomType
from model.booking import Booking

from data_access.base_data_access import BaseDataAccess

class HotelDataAccess(BaseDataAccess):
    
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # User Story 3.1: Hotel hinzufügen
    def create_new_hotel(self, name: str, stars: int, address_id: int = None) -> Hotel:
        sql = """
        INSERT INTO Hotel (Name, Stars, Address_Id) VALUES (?, ?, ?)
        """
        params = (name, stars, address_id)
        last_row_id, row_count = self.execute(sql, params)
        return Hotel(last_row_id, name, stars)

    # Basis Read-Methoden
    def read_hotel_by_id(self, hotel_id: int) -> Hotel | None:
        sql = """
        SELECT h.Hotel_id, h.Name, h.Stars, a.Address_Id, a.Street, a.City, a.Zip_Code
        FROM Hotel h
        LEFT JOIN Address a ON h.Address_Id = a.Address_Id
        WHERE h.Hotel_id = ?
        """
        params = tuple([hotel_id])
        result = self.fetchone(sql, params)
        if result:
            hotel_id, name, stars, address_id, street, city, zip_code = result
            address = None
            if address_id:
                address = Address(address_id, street, city, zip_code)
            return Hotel(hotel_id, name, stars, address)
        return None

    def read_hotel_by_name(self, name: str) -> Hotel | None:
        sql = """
        SELECT h.Hotel_id, h.Name, h.Stars, a.Address_Id, a.Street, a.City, a.Zip_Code
        FROM Hotel h
        LEFT JOIN Address a ON h.Address_Id = a.Address_Id
        WHERE h.Name = ?
        """
        params = tuple([name])
        result = self.fetchone(sql, params)
        if result:
            hotel_id, name, stars, address_id, street, city, zip_code = result
            address = None
            if address_id:
                address = Address(address_id, street, city, zip_code)
            return Hotel(hotel_id, name, stars, address)
        return None

    # User Story 1.1: Hotels nach Stadt durchsuchen
    def read_hotels_by_city(self, city: str) -> list[Hotel]:
        sql = """
        SELECT h.Hotel_id, h.Name, h.Stars, a.Address_Id, a.Street, a.City, a.Zip_Code
        FROM Hotel h
        JOIN Address a ON h.Address_Id = a.Address_Id
        WHERE a.City = ?
        ORDER BY h.Stars DESC, h.Name
        """
        params = tuple([city])
        result = self.fetchall(sql, params)

        hotels = []
        for row in result:
            hotel_id, name, stars, address_id, street, city, zip_code = row
            address = Address(address_id, street, city, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels
    
    # User Story 1.2: Hotels nach Sternen filtern
    def read_hotels_by_stars(self, min_stars: int) -> list[Hotel]:
        sql = """
        SELECT h.Hotel_id, h.Name, h.Stars, a.Address_Id, a.Street, a.City, a.Zip_Code
        FROM Hotel h
        LEFT JOIN Address a ON h.Address_Id = a.Address_Id
        WHERE h.Stars >= ?
        ORDER BY h.Stars DESC, h.Name
        """
        params = tuple([min_stars])
        result = self.fetchall(sql, params)

        hotels = []
        for row in result:
            hotel_id, name, stars, address_id, street, city, zip_code = row
            address = None
            if address_id:
                address = Address(address_id, street, city, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels

    # User Story 1.5: Kombinierte Filter (Stadt + Sterne)
    def read_hotels_by_city_and_stars(self, city: str, min_stars: int) -> list[Hotel]:
        sql = """
        SELECT h.Hotel_id, h.Name, h.Stars, a.Address_Id, a.Street, a.City, a.Zip_Code
        FROM Hotel h
        JOIN Address a ON h.Address_Id = a.Address_Id
        WHERE a.City = ? AND h.Stars >= ?
        ORDER BY h.Stars DESC, h.Name
        """
        params = (city, min_stars)
        result = self.fetchall(sql, params)

        hotels = []
        for row in result:
            hotel_id, name, stars, address_id, street, city, zip_code = row
            address = Address(address_id, street, city, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels

    # User Story 1.3: Hotels mit passender Gästezahl
    def read_hotels_by_city_and_guests(self, city: str, max_guests: int) -> list[Hotel]:
        sql = """
        SELECT DISTINCT h.Hotel_id, h.Name, h.Stars, a.Address_Id, a.Street, a.City, a.Zip_Code
        FROM Hotel h 
        JOIN Room r ON h.Hotel_id = r.Hotel_id
        JOIN Room_Type rt ON r.Type_id = rt.Type_id
        JOIN Address a ON h.Address_id = a.Address_id
        WHERE a.City = ? AND rt.Max_guests >= ?
        ORDER BY h.Stars DESC, h.Name
        """
        params = tuple([city, max_guests])
        result = self.fetchall(sql, params)
        
        hotels = []
        for row in result:
            hotel_id, name, stars, address_id, street, city, zip_code = row
            address = Address(address_id, street, city, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels

    # User Story 1.4: Hotels mit Verfügbarkeit
    def read_available_hotels(self, city: str, check_in: str, check_out: str) -> list[Hotel]:
        sql = """
        SELECT DISTINCT h.Hotel_id, h.Name, h.Stars, a.Address_Id, a.Street, a.City, a.Zip_Code
        FROM Hotel h 
        JOIN Room r ON h.Hotel_id = r.Hotel_id
        JOIN Address a ON h.Address_id = a.Address_id    
        WHERE a.City = ? AND r.Room_id NOT IN (
            SELECT b.Room_id FROM Booking b
            WHERE b.Is_cancelled = 0 AND (
                (b.Check_in_date <= ? AND b.Check_out_date > ?) OR
                (b.Check_in_date < ? AND b.Check_out_date >= ?)
            )
        )
        ORDER BY h.Stars DESC, h.Name
        """
        params = tuple([city, check_in, check_in, check_out, check_out])
        result = self.fetchall(sql, params)
        
        hotels = []
        for row in result:
            hotel_id, name, stars, address_id, street, city, zip_code = row
            address = Address(address_id, street, city, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels

    # User Story 1.5: Kombinierte Suche (alle Filter)
    def search_hotels_combined(self, city: str = None, min_stars: int = None, 
                              max_guests: int = None, check_in: str = None, 
                              check_out: str = None) -> list[Hotel]:
        # Basis SQL
        sql = """
        SELECT DISTINCT h.Hotel_id, h.Name, h.Stars, a.Address_Id, a.Street, a.City, a.Zip_Code
        FROM Hotel h 
        LEFT JOIN Address a ON h.Address_id = a.Address_id
        """
        
        # Conditions und Joins hinzufügen
        conditions = []
        joins = []
        params = []
        
        if city:
            conditions.append("a.City = ?")
            params.append(city)
        
        if min_stars:
            conditions.append("h.Stars >= ?")
            params.append(min_stars)
        
        if max_guests:
            joins.append("JOIN Room r ON h.Hotel_id = r.Hotel_id")
            joins.append("JOIN Room_Type rt ON r.Type_id = rt.Type_id")
            conditions.append("rt.Max_guests >= ?")
            params.append(max_guests)
        
        if check_in and check_out:
            if "JOIN Room r" not in " ".join(joins):
                joins.append("JOIN Room r ON h.Hotel_id = r.Hotel_id")
            conditions.append("""r.Room_id NOT IN (
                SELECT b.Room_id FROM Booking b
                WHERE b.Is_cancelled = 0 AND (
                    (b.Check_in_date <= ? AND b.Check_out_date > ?) OR
                    (b.Check_in_date < ? AND b.Check_out_date >= ?)
                )
            )""")
            params.extend([check_in, check_in, check_out, check_out])
        
        # SQL zusammenbauen
        if joins:
            sql += " " + " ".join(joins)
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        sql += " ORDER BY h.Stars DESC, h.Name"
        
        result = self.fetchall(sql, tuple(params))
        
        hotels = []
        for row in result:
            hotel_id, name, stars, address_id, street, city, zip_code = row
            address = None
            if address_id:
                address = Address(address_id, street, city, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels

    # User Story 3.3: Hotel aktualisieren
    def update_hotel(self, hotel_id: int, name: str = None, stars: int = None) -> bool:
        updates = []
        params = []
        
        if name:
            updates.append("Name = ?")
            params.append(name)
        if stars:
            updates.append("Stars = ?")
            params.append(stars)
        
        if not updates:
            return False
            
        params.append(hotel_id)
        sql = f"UPDATE Hotel SET {', '.join(updates)} WHERE Hotel_id = ?"
        
        last_row_id, row_count = self.execute(sql, tuple(params))
        return row_count > 0

    # User Story 3.2: Hotel löschen
    def delete_hotel(self, hotel_id: int) -> bool:
        sql = "DELETE FROM Hotel WHERE Hotel_id = ?"
        params = tuple([hotel_id])
        last_row_id, row_count = self.execute(sql, params)
        return row_count > 0

    # User Story 8: Alle Hotels für Admin
    def read_all_hotels(self) -> list[Hotel]:
        sql = """
        SELECT h.Hotel_id, h.Name, h.Stars, a.Address_Id, a.Street, a.City, a.Zip_Code
        FROM Hotel h
        LEFT JOIN Address a ON h.Address_Id = a.Address_Id
        ORDER BY h.Name
        """
        result = self.fetchall(sql, tuple())
        
        hotels = []
        for row in result:
            hotel_id, name, stars, address_id, street, city, zip_code = row
            address = None
            if address_id:
                address = Address(address_id, street, city, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels