import os

import model
import data_access

class FacilitiesManager:
    def __init__(self) -> None:
        self.__facilities_dal = data_access.FacilitiesDataAccess()

    def read_facilities_name(self, facility_name: str) -> model.Facilities:
        return self.__facilities_dal.read_facilities_name(facility_id, facility_name)
    
    def update_facilities_name(self, facility_name: str) -> model.Facilities:
        return self.__facilities_dal.update_facilities_name(facility_name)
    
    def delete_facilities(self, facility_id: int) -> model.Facilities:
        return self.__facilities_dal.delete_facilities(facility_id)

    #def insert_facilities(self, facility_id: int) -> model.Facilities:
       # return self.__facilities_dal.insert_facilities(facility_id)