from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
    
    def create_new_address(self, street: str, city: str, zip_code: str) -> Address:
        if not street:
            raise ValueError("Street is required")
        if not city:
            raise ValueError("City is required")
        if not zip_code:
            raise ValueError("Zip Code is required")
            
        sql = """
        INSERT INTO Address (Street, City, Zip_Code) VALUES (?, ?, ?)
        """
        params = (street, city, zip_code)
        last_row_id, row_count = self.execute(sql, params)
        return Address(last_row_id, street, city, zip_code)

    def read_address_by_id(self, address_id: int) -> Address | None:
        sql = """
        SELECT Address_Id, Street, City, Zip_Code FROM Address WHERE Address_Id = ?
        """
        params = tuple([address_id])
        result = self.fetchone(sql, params)
        if result:
            address_id, street, city, zip_code = result
            return Address(address_id, street, city, zip_code)
        return None

    def read_addresses_by_city(self, city: str) -> list[Address]:
        sql = """
        SELECT Address_Id, Street, City, Zip_Code FROM Address WHERE City = ?
        """
        params = tuple([city])
        result = self.fetchall(sql, params)
        return [
            Address(address_id, street, city, zip_code) 
            for address_id, street, city, zip_code in result
        ]

    def update_address(self, address_id: int, street: str = None, 
                      city: str = None, zip_code: str = None) -> bool:
        updates = []
        params = []
        
        if street:
            updates.append("Street = ?")
            params.append(street)
        if city:
            updates.append("City = ?")
            params.append(city)
        if zip_code:
            updates.append("Zip_Code = ?")
            params.append(zip_code)
        
        if not updates:
            return False
            
        params.append(address_id)
        sql = f"UPDATE Address SET {', '.join(updates)} WHERE Address_Id = ?"
        
        last_row_id, row_count = self.execute(sql, tuple(params))
        return row_count > 0

    def delete_address(self, address_id: int) -> bool:
        sql = "DELETE FROM Address WHERE Address_Id = ?"
        params = tuple([address_id])
        last_row_id, row_count = self.execute(sql, params)
        return row_count > 0

    def read_all_addresses(self) -> list[Address]:
        sql = """
        SELECT Address_Id, Street, City, Zip_Code FROM Address ORDER BY City, Street
        """
        result = self.fetchall(sql, tuple())
        return [
            Address(address_id, street, city, zip_code) 
            for address_id, street, city, zip_code in result
        ]