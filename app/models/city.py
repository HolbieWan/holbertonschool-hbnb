from models.base_model import BaseModel
from datetime import datetime

class City(BaseModel):
    def __init__(self, name, country_id, data_manager):
        super().__init__()
        if not name:
            raise ValueError("City name is required!")
        if data_manager.city_exists_with_name_and_country(name, country_id):
            raise ValueError("City name must be unique within the same country")
        if not country_id:
            raise ValueError("Country ID is required!")
        self._name = name
        self._country_id = country_id
        self.data_manager = data_manager

    @staticmethod
    def from_dict(data, data_manager):
        city = City(
            name=data['city_name'],
            country_id=data['country_code'],
            data_manager=data_manager
        )
        city.id = data['city_id']
        city.created_at = datetime.fromisoformat(data['created_at'])
        city.updated_at = datetime.fromisoformat(data['updated_at'])
        return city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.save()

    @property
    def country_id(self):
        return self._country_id

    @country_id.setter
    def country_id(self, value):
        self._country_id = value
        self.save()

    def to_dict(self):
        return {
            "city_id": self.id,
            "city_name": self._name,
            "country_id": self._country_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
